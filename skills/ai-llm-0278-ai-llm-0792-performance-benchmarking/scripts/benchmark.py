#!/usr/bin/env python3
import timeit

def benchmark(fn_name, slow_fn, fast_fn, setup_code, number=10000):
    print(f"Benchmarking {fn_name}...")
    slow_time = timeit.timeit(slow_fn, setup=setup_code, globals=globals(), number=number)
    fast_time = timeit.timeit(fast_fn, setup=setup_code, globals=globals(), number=number)

    print(f"  Slow: {slow_time:.5f}s")
    print(f"  Fast: {fast_time:.5f}s")
    print(f"  Speedup: {slow_time/fast_time:.2f}x\n")

if __name__ == '__main__':
    setup = '''
import random
items = [random.randint(0, 1000) for _ in range(1000)]
items_set = set(items)
target = 500
    '''

    def find_slow():
        global items, target
        return [i for i in items if i == target]

    def find_fast():
        global items_set, target
        return target in items_set

    benchmark('List vs Set Lookup', 'find_slow()', 'find_fast()', setup)
