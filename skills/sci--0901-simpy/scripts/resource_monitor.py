#!/usr/bin/env python3
import simpy
import csv
from typing import List, Dict

class ResourceMonitor:
    def __init__(self, env, resource, name):
        self.env = env
        self.resource = resource
        self.name = name
        self.data: List[Dict] = []
        self.env.process(self.monitor())

    def monitor(self):
        while True:
            self.data.append({
                'time': self.env.now,
                'resource': self.name,
                'capacity': self.resource.capacity,
                'in_use': self.resource.count,
                'queue_length': len(self.resource.queue)
            })
            yield self.env.timeout(1)

    def report(self):
        print(f"\n--- Resource Monitor Report: {self.name} ---")
        if not self.data:
            print("No data collected.")
            return

        total_time = len(self.data)
        avg_in_use = sum(d['in_use'] for d in self.data) / total_time
        avg_queue = sum(d['queue_length'] for d in self.data) / total_time
        max_queue = max(d['queue_length'] for d in self.data)
        utilization = avg_in_use / self.resource.capacity * 100

        print(f"Average Utilization: {utilization:.2f}%")
        print(f"Average Queue Length: {avg_queue:.2f}")
        print(f"Maximum Queue Length: {max_queue}")

    def export_csv(self, filename):
        if not self.data:
            return

        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)

class MultiResourceMonitor:
    def __init__(self, env, resources, names):
        self.monitors = [ResourceMonitor(env, res, name) for res, name in zip(resources, names)]

    def report(self):
        for monitor in self.monitors:
            monitor.report()

    def export_csv(self, filename_prefix):
        for i, monitor in enumerate(self.monitors):
            monitor.export_csv(f"{filename_prefix}_{monitor.name}.csv")

class ContainerMonitor:
    def __init__(self, env, container, name):
        self.env = env
        self.container = container
        self.name = name
        self.data: List[Dict] = []
        self.env.process(self.monitor())

    def monitor(self):
        while True:
            self.data.append({
                'time': self.env.now,
                'container': self.name,
                'capacity': self.container.capacity,
                'level': self.container.level
            })
            yield self.env.timeout(1)

    def report(self):
        print(f"\n--- Container Monitor Report: {self.name} ---")
        if not self.data:
            print("No data collected.")
            return

        total_time = len(self.data)
        avg_level = sum(d['level'] for d in self.data) / total_time
        min_level = min(d['level'] for d in self.data)
        max_level = max(d['level'] for d in self.data)

        print(f"Average Level: {avg_level:.2f}")
        print(f"Minimum Level: {min_level}")
        print(f"Maximum Level: {max_level}")

    def export_csv(self, filename):
        if not self.data:
            return

        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)

if __name__ == '__main__':
    def test_simulation():
        env = simpy.Environment()
        resource = simpy.Resource(env, capacity=2)
        monitor = ResourceMonitor(env, resource, "TestServer")

        def process(env, resource):
            while True:
                with resource.request() as req:
                    yield req
                    yield env.timeout(2)

        env.process(process(env, resource))
        env.run(until=10)

        monitor.report()

    test_simulation()
