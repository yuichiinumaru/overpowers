import os
import yaml

class MigrationMapper:
    """Helper to map legacy commands to agent-based definitions."""
    def __init__(self, commands_dir):
        self.commands_dir = commands_dir

    def parse_command(self, filename):
        """Mock parsing of a legacy command file."""
        # In a real scenario, this would read the .md command file
        # and extract its intent, tools used, etc.
        name = os.path.splitext(filename)[0].replace('$', ' ').title()
        return {
            'role': 'coordinator',
            'name': name,
            'responsibilities': [f'Handle tasks related to {name}'],
            'capabilities': [filename.split('$')[-1]],
            'tools': {
                'allowed': ['Read', 'Bash'],
                'restricted': ['Write', 'Edit']
            },
            'triggers': [
                {'pattern': filename.split('$')[-1], 'priority': 'medium'}
            ]
        }

    def generate_agent_yaml(self, agent_data):
        return yaml.dump(agent_data, sort_keys=False)

if __name__ == "__main__":
    import sys
    mapper = MigrationMapper(".claude/commands")
    example_cmd = "coordination$init.md"
    data = mapper.parse_command(example_cmd)
    print(f"--- Agent Definition for {example_cmd} ---")
    print(mapper.generate_agent_yaml(data))
