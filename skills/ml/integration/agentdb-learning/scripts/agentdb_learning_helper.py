import argparse

class AgentDBLearningHelper:
    """Helper to generate AgentDB learning plugin commands."""
    
    @staticmethod
    def get_create_cmd(template, name, output_dir=None, dry_run=False):
        cmd = f"npx agentdb@latest create-plugin -t {template} -n {name}"
        if output_dir:
            cmd += f" -o {output_dir}"
        if dry_run:
            cmd += " --dry-run"
        return cmd

    @staticmethod
    def get_info_cmd(name):
        return f"npx agentdb@latest plugin-info {name}"

    @staticmethod
    def get_list_cmd():
        return "npx agentdb@latest list-plugins"

    @staticmethod
    def get_templates_cmd():
        return "npx agentdb@latest list-templates"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AgentDB Learning Plugin Command Generator")
    parser.add_argument("--action", choices=['create', 'info', 'list', 'templates'], default='list')
    parser.add_argument("--template", default="decision-transformer")
    parser.add_argument("--name", default="my-agent")
    
    args = parser.parse_args()
    helper = AgentDBLearningHelper()
    
    if args.action == 'create':
        print(helper.get_create_cmd(args.template, args.name))
    elif args.action == 'info':
        print(helper.get_info_cmd(args.name))
    elif args.action == 'list':
        print(helper.get_list_cmd())
    elif args.action == 'templates':
        print(helper.get_templates_cmd())
