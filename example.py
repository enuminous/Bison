from bison import Component, BisonSystem

system = BisonSystem({
    "interactive": Component(capacity=50, queue_limit=60, criticality=1.0),
    "background": Component(capacity=40, queue_limit=100, criticality=0.2),
})

loads = [
    {"interactive":30,"background":20},
    {"interactive":45,"background":35},
    {"interactive":60,"background":50},
    {"interactive":80,"background":70},
]

for load in loads:
    print(system.step(load))
