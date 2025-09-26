# Re-import required libraries due to kernel reset
import random
import numpy as np
from collections import defaultdict

# Optional progress bar via tqdm (fallback to simple prints if unavailable)
try:
    from tqdm import tqdm  # type: ignore
    _TQDM_AVAILABLE = True
except Exception:
    tqdm = None  # type: ignore
    _TQDM_AVAILABLE = False

# Updated simulation: doubles only count after the first 3 rolls
def simulate_by_early_sevens_updated(trials=1000000, show_progress=True):
    results_by_sevens = defaultdict(list)

    iterable = tqdm(range(trials), total=trials, unit="trial", desc="Simulating") if _TQDM_AVAILABLE and show_progress else range(trials)
    for i in iterable:
        total_sum = 0
        if show_progress and not _TQDM_AVAILABLE and trials > 0 and (i + 1) % max(1, trials // 100) == 0:
            print(f"Simulating: {((i + 1) / trials):.0%}")
        rolls = 0
        early_sevens = 0

        while True:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            roll_sum = die1 + die2
            rolls += 1

            # Checking stopping condition first
            if rolls > 3 and roll_sum == 7:
                # Any sevens after the first 3 rolls immediately ends the round
                results_by_sevens[early_sevens].append(total_sum)
                break

            # Special behavior for the first 3 rolls
            if rolls <=3:
                # A seven behavior
                if roll_sum == 7:
                    total_sum += 70
                    early_sevens += 1
                    continue
                else:
                    total_sum += roll_sum
                    continue
            else:
                # Behavior for the rolls beyond the third
                if die1 == die2:
                    # Doubles were rolled
                    total_sum *= 2
                else:
                    # Doubles were not rolled
                    total_sum += roll_sum

                # The stopping condition has already been checked

    # Calculate expected values by number of early sevens
    expected_values = {
        k: np.mean(v) for k, v in results_by_sevens.items()
    }

    return expected_values

# Run the updated simulation
updated_expected_values_by_early_sevens = simulate_by_early_sevens_updated()
print(updated_expected_values_by_early_sevens)


# Based on a 1 million trials simulation the values are:
# Zero 7s in the first 3 rolls: 446
# One 7 in the first 3 rolls: 1546
# Two 7s in the first 3 rolls: 2851
# Three 7s in the first 3 rolls: 2623
