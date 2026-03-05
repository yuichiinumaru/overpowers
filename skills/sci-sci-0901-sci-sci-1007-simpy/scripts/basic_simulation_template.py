import simpy
import random

class SimulationConfig:
    def __init__(self, num_resources=1, sim_time=100, arrival_rate=2, service_rate=3):
        self.num_resources = num_resources
        self.sim_time = sim_time
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate

class Statistics:
    def __init__(self):
        self.wait_times = []

    def report(self):
        if not self.wait_times:
            print("No data collected.")
            return
        avg_wait = sum(self.wait_times) / len(self.wait_times)
        print(f"Total Customers: {len(self.wait_times)}")
        print(f"Average Wait Time: {avg_wait:.2f}")

def customer(env, name, server, stats, service_rate):
    arrival_time = env.now
    with server.request() as req:
        yield req
        wait_time = env.now - arrival_time
        stats.wait_times.append(wait_time)
        yield env.timeout(random.expovariate(1.0 / service_rate))

def customer_generator(env, server, stats, arrival_rate, service_rate):
    i = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / arrival_rate))
        i += 1
        env.process(customer(env, f'Customer {i}', server, stats, service_rate))

def run_simulation(config):
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=config.num_resources)
    stats = Statistics()
    env.process(customer_generator(env, server, stats, config.arrival_rate, config.service_rate))
    env.run(until=config.sim_time)
    return stats

if __name__ == "__main__":
    config = SimulationConfig(num_resources=2, sim_time=50)
    stats = run_simulation(config)
    stats.report()
