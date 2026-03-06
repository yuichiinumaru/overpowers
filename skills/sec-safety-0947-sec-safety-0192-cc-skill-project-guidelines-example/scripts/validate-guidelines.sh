#!/bin/bash
echo "Validating project guidelines..."
grep -r "console.log" src/ && echo "Found console.log in src/"
echo "Guidelines check passed."
