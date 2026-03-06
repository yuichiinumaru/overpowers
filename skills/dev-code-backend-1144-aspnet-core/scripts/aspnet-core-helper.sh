#!/bin/bash
# Helper script to perform quick checks on ASP.NET Core projects

if [ "$1" == "check-target" ]; then
    if ls *.csproj 1> /dev/null 2>&1; then
        grep -oP '(?<=<TargetFramework>).*?(?=</TargetFramework>)' *.csproj
    else
        echo "No .csproj file found in current directory."
    fi
elif [ "$1" == "list-refs" ]; then
    dotnet list reference
else
    echo "Usage: $0 [check-target|list-refs]"
    echo "  check-target : Print the TargetFramework from the current csproj"
    echo "  list-refs    : List project references"
    exit 1
fi
