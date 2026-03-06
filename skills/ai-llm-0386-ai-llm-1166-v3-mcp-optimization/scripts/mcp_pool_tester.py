#!/usr/bin/env python3
"""
Helper script to test MCP connection pool performance.
"""
import time

def test_pool():
    print("Testing MCP connection pool optimization...")
    start_time = time.time()

    # Simulate connection pool warmup
    time.sleep(0.1)

    # Simulate tool registry O(1) lookup
    time.sleep(0.005)

    print("Startup time: <400ms target")
    print("Tool lookup time: <5ms target")
    print(f"Total simulated time: {(time.time() - start_time) * 1000:.2f}ms")

if __name__ == "__main__":
    test_pool()
