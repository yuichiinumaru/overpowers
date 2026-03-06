#!/bin/bash
# Generate basic mTLS certificates for testing
dir=${1:-./certs}
mkdir -p "$dir"

echo "Generating CA certificate..."
openssl req -new -x509 -days 365 -nodes -out "$dir/ca.crt" -keyout "$dir/ca.key" -subj "/CN=MyRootCA" 2>/dev/null

echo "Generating Server certificate..."
openssl req -new -nodes -out "$dir/server.csr" -keyout "$dir/server.key" -subj "/CN=server" 2>/dev/null
openssl x509 -req -in "$dir/server.csr" -days 365 -CA "$dir/ca.crt" -CAkey "$dir/ca.key" -CAcreateserial -out "$dir/server.crt" 2>/dev/null

echo "Generating Client certificate..."
openssl req -new -nodes -out "$dir/client.csr" -keyout "$dir/client.key" -subj "/CN=client" 2>/dev/null
openssl x509 -req -in "$dir/client.csr" -days 365 -CA "$dir/ca.crt" -CAkey "$dir/ca.key" -CAcreateserial -out "$dir/client.crt" 2>/dev/null

echo "mTLS certificates generated in $dir/"
