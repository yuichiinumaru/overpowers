#!/usr/bin/env python3
import sys

def generate_orpc_contract(domain, route_name):
    code = f"""import {{ base }} from '../base';
import {{ type }} from '@orpc/contract';
import {{ z }} from 'zod';

export const {route_name} = base
  .path('/{domain}/{route_name}')
  .method('GET')
  .input(z.object({{
    params: z.object({{
      id: z.string(),
    }}),
    query: z.object({{
      limit: z.number().optional(),
    }}).optional(),
  }}))
  .output(z.object({{
    id: z.string(),
    name: z.string(),
  }}));
"""
    print(code)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: orpc_scaffold.py <domain> <route_name>")
        sys.exit(1)
    
    generate_orpc_contract(sys.argv[1], sys.argv[2])
