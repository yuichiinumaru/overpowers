#!/bin/bash
# Helper script for sec-safety-0918-sec-safety-0039-agentdb-learning

echo "Helper for sec-safety-0918-sec-safety-0039-agentdb-learning"

# Command examples from SKILL.md:
# # Interactive wizard
# npx agentdb@latest create-plugin
# # Use specific template
# npx agentdb@latest create-plugin -t decision-transformer -n my-agent
# # Preview without creating
# npx agentdb@latest create-plugin -t q-learning --dry-run
# # Custom output directory
# npx agentdb@latest create-plugin -t actor-critic -o ./plugins
# # Show all plugin templates
# npx agentdb@latest list-templates
# # Available templates:
# # - decision-transformer (sequence modeling RL - recommended)
# # - q-learning (value-based learning)
# # - sarsa (on-policy TD learning)
# # - actor-critic (policy gradient with baseline)
# # - curiosity-driven (exploration-based)
# # List installed plugins
# npx agentdb@latest list-plugins
# # Get plugin information
# npx agentdb@latest plugin-info my-agent
# # Shows: algorithm, configuration, training status
# npx agentdb@latest create-plugin -t decision-transformer -n dt-agent
# npx agentdb@latest create-plugin -t q-learning -n q-agent
# npx agentdb@latest create-plugin -t sarsa -n sarsa-agent
# npx agentdb@latest create-plugin -t actor-critic -n ac-agent
# # Create plugin
# npx agentdb@latest create-plugin -t decision-transformer -n my-plugin
# # List plugins
# npx agentdb@latest list-plugins
# # Get plugin info
# npx agentdb@latest plugin-info my-plugin
# # List templates
# npx agentdb@latest list-templates
# # Enable quantization for faster inference
# # Use binary quantization (32x faster)
