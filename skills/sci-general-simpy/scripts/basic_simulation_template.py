#!/usr/bin/env python3
import simpy
import random
from dataclasses import dataclass

@dataclass
class SimulationConfig:
    num_resources: int = 1
    sim_time: int = 20
    arrival_rate: float = 1.0
    service_rate: float = 2.0

class Statistics:
    def __init__(self):
        self.wait_times = []
        self.service_times = []
        self.total_customers = 0

    def report(self):
        print("\n--- Simulation Report ---")
        print(f"Total customers served: {self.total_customers}")
        if self.wait_times:
            avg_wait = sum(self.wait_times) / len(self.wait_times)
            print(f"Average wait time: {avg_wait:.2f}")
        if self.service_times:
            avg_service = sum(self.service_times) / len(self.service_times)
            print(f"Average service time: {avg_service:.2f}")

def customer(env, name, resource, config, stats):
    arrival = env.now
    with resource.request() as req:
        yield req
        wait = env.now - arrival
        stats.wait_times.append(wait)

        service_time = random.expovariate(1.0 / config.service_rate)
        yield env.timeout(service_time)

        stats.service_times.append(service_time)
        stats.total_customers += 1

def setup(env, config, stats):
    resource = simpy.Resource(env, capacity=config.num_resources)
    i = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / config.arrival_rate))
        i += 1
        env.process(customer(env, f'Customer {i}', resource, config, stats))

def run_simulation(config):
    env = simpy.Environment()
    stats = Statistics()
    env.process(setup(env, config, stats))
    env.run(until=config.sim_time)
    return stats

if __name__ == '__main__':
    config = SimulationConfig()
    config.num_resources = 2
    config.sim_time = 100
    stats = run_simulation(config)
    stats.report()
