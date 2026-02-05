
/**
 * Destructive Command Blocker Hook
 *
 * Based on 'destructive_command_guard' (Rust).
 * Intercepts shell commands that match known destructive patterns.
 */

interface DestructivePattern {
  id: string;
  regex: RegExp;
  description: string;
  severity: "Critical" | "High" | "Medium";
  mitigation: string;
}

const PATTERNS: DestructivePattern[] = [
  // --- Filesystem ---
  {
    id: "rm-rf-root",
    regex: /rm\s+(-[rR][fF]|-fr)\s+(\/|\/\*)/,
    description: "rm -rf / is extremely dangerous and will wipe the system.",
    severity: "Critical",
    mitigation: "Check path variables. Never run on root."
  },
  {
    id: "rm-rf-home",
    regex: /rm\s+(-[rR][fF]|-fr)\s+~\/?/,
    description: "rm -rf ~ is extremely dangerous and will wipe your home directory.",
    severity: "Critical",
    mitigation: "Check path variables. Never run on home."
  },
  {
    id: "mkfs",
    regex: /mkfs(\.[a-z0-9]+)?\s+/,
    description: "mkfs formats a partition and erases all data.",
    severity: "Critical",
    mitigation: "Ensure you are targeting the correct device/loopback file."
  },
  {
    id: "dd-device",
    regex: /dd\s+.*of=\/dev\/(sd[a-z]|nvme\d+n\d+)/,
    description: "dd to a physical block device will overwrite data.",
    severity: "Critical",
    mitigation: "Verify target device. Use a loopback file if testing."
  },
  {
    id: "chmod-777",
    regex: /chmod\s+(?:.*\s+)?["'=]?0*777(?:[\s"']|$)/,
    description: "chmod 777 makes files world-writable.",
    severity: "High",
    mitigation: "Use chmod 755 or u+x."
  },
  {
    id: "chmod-recursive-root",
    regex: /chmod\s+(?:.*(?:-[rR]|--recursive)).*\s+\/(?:$|bin|boot|dev|etc|lib|opt|proc|root|run|sbin|sys|usr|var)\b/,
    description: "Recursive chmod on system directories breaks the OS.",
    severity: "High",
    mitigation: "Target specific files."
  },

  // --- CI/CD & Cloud ---
  {
    id: "circleci-context-delete",
    regex: /circleci(?:\s+--?\S+(?:\s+\S+)?)*\s+context\s+delete\b/,
    description: "Deleting CircleCI contexts removes secrets irreversibly.",
    severity: "Critical",
    mitigation: "List contexts first. Verify backup of secrets."
  },
  {
    id: "aws-s3-rb-force",
    regex: /aws\s+s3\s+rb\s+.*--force/,
    description: "aws s3 rb --force deletes a bucket and ALL its objects.",
    severity: "High",
    mitigation: "List objects first. Delete objects explicitly if needed."
  },
  {
    id: "terraform-destroy-auto-approve",
    regex: /terraform\s+destroy\s+.*-auto-approve/,
    description: "Automated terraform destroy skips safety checks.",
    severity: "High",
    mitigation: "Run plan first. Remove auto-approve."
  }
];

export function checkCommand(command: string): string | null {
  for (const pattern of PATTERNS) {
    if (pattern.regex.test(command)) {
      return `[BLOCKED] ${pattern.description}\nSeverity: ${pattern.severity}\nMitigation: ${pattern.mitigation}`;
    }
  }
  return null;
}

// Example usage in a hook context:
// const blocked = checkCommand(inputCommand);
// if (blocked) throw new Error(blocked);
