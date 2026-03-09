import random


def simulate_optimization():

    ctr_change = random.randint(5, 15)
    cpc_change = random.randint(5, 12)

    return {
        "ctr_improvement": ctr_change,
        "cpc_reduction": cpc_change
    }