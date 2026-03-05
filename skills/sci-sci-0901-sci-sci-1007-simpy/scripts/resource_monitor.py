import simpy
import csv

class ResourceMonitor:
    """Monitor a single SimPy resource."""
    def __init__(self, env, resource, name):
        self.env = env
        self.resource = resource
        self.name = name
        self.data = []
        self.env.process(self._monitor())

    def _monitor(self):
        while True:
            self.data.append((self.env.now, self.resource.count, len(self.resource.queue)))
            yield self.env.timeout(1)

    def report(self):
        print(f"--- Report for {self.name} ---")
        if not self.data:
            print("No data collected.")
            return
        
        avg_usage = sum(d[1] for d in self.data) / len(self.data)
        avg_queue = sum(d[2] for d in self.data) / len(self.data)
        print(f"Average Usage: {avg_usage:.2f}")
        print(f"Average Queue Length: {avg_queue:.2f}")

    def export_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'Usage', 'Queue'])
            writer.writerows(self.data)
        print(f"Data exported to {filename}")

class ContainerMonitor:
    """Monitor a SimPy container."""
    def __init__(self, env, container, name):
        self.env = env
        self.container = container
        self.name = name
        self.data = []
        self.env.process(self._monitor())

    def _monitor(self):
        while True:
            self.data.append((self.env.now, self.container.level))
            yield self.env.timeout(1)

    def report(self):
        print(f"--- Report for Container: {self.name} ---")
        if not self.data:
            print("No data collected.")
            return
        
        avg_level = sum(d[1] for d in self.data) / len(self.data)
        print(f"Average Level: {avg_level:.2f}")

    def export_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'Level'])
            writer.writerows(self.data)
        print(f"Data exported to {filename}")
