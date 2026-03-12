#!/usr/bin/env bash

# Expo Component Scaffolding Script
# Creates a new Expo React Native component
# Usage: ./expo_scaffold.sh components/Button

COMPONENT_PATH=$1

if [ -z "$COMPONENT_PATH" ]; then
  echo "Usage: ./expo_scaffold.sh <path/ComponentName>"
  exit 1
fi

COMPONENT_DIR=$(dirname "$COMPONENT_PATH")
COMPONENT_NAME=$(basename "$COMPONENT_PATH")

mkdir -p "$COMPONENT_DIR"

cat <<EOF > "$COMPONENT_PATH.tsx"
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface ${COMPONENT_NAME}Props {
  title?: string;
}

export const ${COMPONENT_NAME} = ({ title = '${COMPONENT_NAME}' }: ${COMPONENT_NAME}Props) => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>{title}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
    borderRadius: 8,
    backgroundColor: '#fff',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  text: {
    fontSize: 16,
    color: '#333',
    fontWeight: '500',
  },
});
EOF

echo "Created Expo component: $COMPONENT_PATH.tsx"
