#!/bin/bash
# Generate Next.js App Router boilerplate route
route_dir=$1

if [ -z "$route_dir" ]; then
    echo "Usage: $0 <route_path>"
    return 1 2>/dev/null || true
fi

mkdir -p "$route_dir"
cat << 'TPL' > "$route_dir/page.tsx"
export default function Page() {
  return (
    <main>
      <h1>New Route</h1>
    </main>
  );
}
TPL
echo "Generated Next.js route at $route_dir/page.tsx"
