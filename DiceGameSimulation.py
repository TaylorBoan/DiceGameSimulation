import random
import numpy as np
from collections import defaultdict

def simulate_by_early_sevens(trials=100000):
    results_by_sevens = defaultdict(list)

    for _ in range(trials):
        total_sum = 0
        rolls = 0
        early_sevens = 0
        while True:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            roll_sum = die1 + die2
            rolls += 1

            # Check for doubles
            if die1 == die2:
                total_sum *= 2

            # Check for sum of 7
            if rolls <= 3 and roll_sum == 7:
                total_sum += 70
                early_sevens += 1
            elif rolls > 3 and roll_sum == 7:
                results_by_sevens[early_sevens].append(total_sum)
                break

            # Add roll sum only if not doubles
            if die1 != die2:
                total_sum += roll_sum

    # Calculate expected values by early_sevens count
    expected_values = {}
    for k, values in results_by_sevens.items():
        expected_values[k] = np.mean(values)

    return expected_values

# Run simulation and collect expected values
expected_values_by_early_sevens = simulate_by_early_sevens()
expected_values_by_early_sevens
