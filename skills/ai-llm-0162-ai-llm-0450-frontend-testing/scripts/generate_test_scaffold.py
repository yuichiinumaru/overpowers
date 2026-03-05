#!/usr/bin/env python3
import sys
import os

def generate_scaffold(component_name):
    template = f"""import {{ render, screen, fireEvent, waitFor }} from '@testing-library/react'
import {component_name} from './index'

describe('{component_name}', () => {{
  beforeEach(() => {{
    vi.clearAllMocks()
  }})

  describe('Rendering', () => {{
    it('should render without crashing', () => {{
      const props = {{ title: 'Test' }}
      render(<{component_name} {{...props}} />)
      expect(screen.getByText('Test')).toBeInTheDocument()
    }})
  }})

  describe('Props', () => {{
    it('should handle basic props', () => {{
      // Add prop tests here
    }})
  }})

  describe('User Interactions', () => {{
    it('should handle events', () => {{
      // const handleClick = vi.fn()
      // render(<{component_name} onClick={{handleClick}} />)
    }})
  }})

  describe('Edge Cases', () => {{
    it('should handle boundary conditions', () => {{
      // Add edge case tests here
    }})
  }})
}})
"""
    file_name = f"{component_name}.spec.tsx"
    with open(file_name, "w") as f:
        f.write(template)
    print(f"Generated test scaffold: {file_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_test_scaffold.py <ComponentName>")
        sys.exit(1)
    generate_scaffold(sys.argv[1])
