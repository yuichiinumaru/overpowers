import os
import time
import json
from pathlib import Path

class APIKeyRotator:
    """
    Advanced API Key Rotator.
    Manages active keys, places rate-limited keys in a 60s cooldown (geladeira), 
    blacklists permanently invalid keys, and hot-reloads new keys from .env.
    """
    def __init__(self, initial_keys, env_file_path=None, env_var_name="GEMINI_API_KEY", blacklist_file=None):
        self.env_file_path = env_file_path
        self.env_var_name = env_var_name
        if blacklist_file:
            self.blacklist_file = Path(blacklist_file)
        elif env_file_path:
            self.blacklist_file = Path(env_file_path).parent / ".docs" / "tasks" / "planning" / "invalid_api_keys.json"
        else:
            self.blacklist_file = None
            
        self.active_keys = set()
        self.cooldown_keys = {}  # key -> timestamp when it comes out of cooldown
        self.invalid_keys = set()
        
        self.ordered_active_keys = []
        
        self.last_env_check = time.time()
        self.env_check_interval = 60  # Check .env every 60 seconds
        
        self._load_blacklist()
        self._add_keys(initial_keys)

    def _load_blacklist(self):
        if self.blacklist_file and self.blacklist_file.exists():
            try:
                with open(self.blacklist_file, 'r') as f:
                    data = json.load(f)
                    self.invalid_keys = set(data.get("invalid_keys", []))
            except Exception:
                pass

    def _save_blacklist(self):
        if self.blacklist_file:
            try:
                self.blacklist_file.parent.mkdir(parents=True, exist_ok=True)
                with open(self.blacklist_file, 'w') as f:
                    json.dump({"invalid_keys": list(self.invalid_keys)}, f, indent=2)
            except Exception:
                pass

    def clear_blacklist(self):
        self.invalid_keys = set()
        self._save_blacklist()
        print("🧹 API Key Blacklist cleared.")

    def _add_keys(self, keys):
        added_count = 0
        for k in keys:
            k = k.strip().strip('"').strip("'")
            if k and k not in self.active_keys and k not in self.invalid_keys and k not in self.cooldown_keys:
                self.active_keys.add(k)
                self.ordered_active_keys.append(k)
                added_count += 1
        return added_count

    def _check_hot_reload(self, force=False):
        """Check .env file for new keys."""
        if not self.env_file_path or not self.env_file_path.exists():
            return
            
        now = time.time()
        if not force and (now - self.last_env_check) < self.env_check_interval:
            return
            
        self.last_env_check = now
        try:
            with open(self.env_file_path, "r") as f:
                for line in f:
                    if line.startswith(f"{self.env_var_name}="):
                        keys_str = line.split("=", 1)[1].strip().strip('"').strip("'")
                        new_keys = [k.strip() for k in keys_str.split(',') if k.strip()]
                        added = self._add_keys(new_keys)
                        if added > 0:
                            print(f"🔄 Hot reload: {added} new keys detected and added! Active base: {len(self.active_keys)}")
                        break
        except Exception:
            pass

    def _update_cooldowns(self):
        """Move keys from cooldown back to active if time has passed."""
        now = time.time()
        recovered_keys = []
        for key, unfreeze_time in list(self.cooldown_keys.items()):
            if now >= unfreeze_time:
                recovered_keys.append(key)
                
        for key in recovered_keys:
            self.cooldown_keys.pop(key, None)
            self.active_keys.add(key)
            self.ordered_active_keys.append(key)
            print(f"❄️  Key recovered from cooldown! Active keys back to: {len(self.active_keys)}")

    def get_next_key(self):
        """Returns the next available API key, handling wait states if exhausted."""
        self._check_hot_reload()
        self._update_cooldowns()
        
        backoff = 60
        while not self.ordered_active_keys:
            print(f"⏳ All keys exhausted (Cooldown: {len(self.cooldown_keys)}, Invalid: {len(self.invalid_keys)}).")
            self._check_hot_reload(force=True)
            self._update_cooldowns()
            
            if self.ordered_active_keys:
                break
                
            if self.cooldown_keys:
                # Wait until the next key is ready
                next_ready = min(self.cooldown_keys.values())
                wait_time = max(1.0, next_ready - time.time())
                print(f"💤 Sleeping for {wait_time:.1f}s until a key recovers from the geladeira...")
                time.sleep(wait_time)
            else:
                # No keys in cooldown, none active. Just wait with exponential backoff and check .env
                print(f"⚠️ No active or recovering keys. Please add keys to .env. Sleeping for {backoff}s...")
                time.sleep(backoff)
                backoff = int(backoff * 2)  # Ad infinitum exponential backoff
                
            self._update_cooldowns()
            
        # We have at least one active key
        key = self.ordered_active_keys.pop(0)
        self.ordered_active_keys.append(key)
        return key

    def report_error(self, key, error_type="RATE_LIMIT"):
        """
        Report an error for a key.
        error_type: "RATE_LIMIT" (429) or "INVALID" (401/403/400 API_KEY_INVALID)
        """
        if key in self.active_keys:
            self.active_keys.remove(key)
            if key in self.ordered_active_keys:
                self.ordered_active_keys.remove(key)
                
        if error_type == "INVALID":
            print("🚫 Key marked as INVALID and blacklisted permanently.")
            self.invalid_keys.add(key)
            self._save_blacklist()
        elif error_type == "RATE_LIMIT":
            print("🧊 Key hit rate limit, placing in 'geladeira' for 60s.")
            self.cooldown_keys[key] = time.time() + 60
            
    def get_key_count(self):
        """Returns total valid keys (active + cooldown)."""
        return len(self.active_keys) + len(self.cooldown_keys)


def get_rotator_from_env(env_var_name="GEMINI_API_KEY", blacklist_file=None):
    """
    Creates an APIKeyRotator from an environment variable and checks the local .env.
    """
    project_root = Path(__file__).resolve().parent.parent
    env_file = project_root / ".env"
    
    keys_str = os.environ.get(env_var_name, "")
    if not keys_str and env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                if line.startswith(f"{env_var_name}="):
                    keys_str = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
                    
    initial_keys = [k.strip() for k in keys_str.split(',')] if keys_str else []
    return APIKeyRotator(initial_keys, env_file_path=env_file, env_var_name=env_var_name, blacklist_file=blacklist_file)

