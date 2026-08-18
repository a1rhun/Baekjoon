import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm, numbers)

def solution(signals):
    periods = [g + y + r for g, y, r in signals]
    total_lcm = lcm_list(periods)

    for t in range(1, total_lcm + 1):
        all_yellow = True

        for g, y, r in signals:
            period = g + y + r
            mod = t % period

            if not (g <= mod <= g + y - 1):
                all_yellow = False
                break

        if all_yellow:
            return t + 1

    return -1