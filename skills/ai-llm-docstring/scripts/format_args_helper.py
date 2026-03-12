#!/usr/bin/env python3
"""
Help format the Args section of a PyTorch docstring.
"""
import sys

def format_arg(name, type_str, description, optional=False, default=None):
    type_suffix = ", optional" if optional else ""
    full_type = f"({type_str}{type_suffix})"
    
    line = f"    {name} {full_type}: {description}"
    if default is not None:
        line += f" Default: ``{default}``"
    return line

def main():
    print("PyTorch Args Section Helper")
    print("Enter argument details (leave name empty to finish):")
    
    args_lines = ["Args:"]
    while True:
        name = input("\nArgument name: ").strip()
        if not name:
            break
        
        type_str = input("Type (e.g. Tensor, int): ").strip()
        desc = input("Description: ").strip()
        is_opt = input("Optional? (y/n): ").lower().startswith('y')
        default = None
        if is_opt:
            default = input("Default value: ").strip()
            
        args_lines.append(format_arg(name, type_str, desc, is_opt, default))
        
    print("\n" + "-" * 20 + " FORMATTED ARGS " + "-" * 20)
    print("\n".join(args_lines))
    print("-" * 56)

if __name__ == "__main__":
    main()
