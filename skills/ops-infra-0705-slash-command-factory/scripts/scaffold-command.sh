#!/bin/bash

# Helper script to scaffold a new CLI slash command
# Usage: ./scaffold-command.sh <name> <type>
# Types: bash, python

NAME=$1
TYPE=${2:-"bash"}

if [[ -z "$NAME" ]]; then
  echo "Usage: $0 <name> [type]"
  echo "Types: bash, python"
  exit 1
fi

case $TYPE in
  bash)
    cat <<EOF > "${NAME}.sh"
#!/bin/bash

# Command: /${NAME}
# Description: Description of what this command does

if [[ \$# -lt 1 ]]; then
  echo "Usage: /${NAME} <args>"
  exit 1
fi

echo "Executing /${NAME} with args: \$@"
# Add logic here
EOF
    chmod +x "${NAME}.sh"
    echo "Scaffolded Bash command: ${NAME}.sh"
    ;;
  python)
    cat <<EOF > "${NAME}.py"
import sys

def main():
    """
    Command: /${NAME}
    Description: Description of what this command does
    """
    if len(sys.argv) < 2:
        print("Usage: /${NAME} <args>")
        sys.exit(1)
    
    print(f"Executing /${NAME} with args: {sys.argv[1:]}")
    # Add logic here

if __name__ == "__main__":
    main()
EOF
    echo "Scaffolded Python command: ${NAME}.py"
    ;;
  *)
    echo "Invalid type: $TYPE. Use bash or python."
    exit 1
    ;;
esac
