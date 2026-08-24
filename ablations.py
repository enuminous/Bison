from bison import Component, BisonSystem

def run(with_queue_limit=True):
    qlim = 100 if with_queue_limit else 1e9
    components = {
        "critical": Component(capacity=100, queue_limit=qlim, criticality=1.0)
    }
    sys = BisonSystem(components, critical_latency_limit=1.8)
    out = None
    for _ in range(10):
        out = sys.step({"critical":150})
    return out

if __name__ == "__main__":
    full = run(True)
    ablated = run(False)
    print("full violations:", full["total_violations"])
    print("no practical queue bound violations:", ablated["total_violations"])
