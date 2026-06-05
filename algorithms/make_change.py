"""
Problem: For amount n, give change using the least possible number of coins.
"""
from math import floor

DENOMINATIONS = [0.01, 0.05, 0.1, 0.25, 1, 2]

def solution(input):
    result = {
        "0.01": 0,
        "0.05": 0,
        "0.1": 0,
        "0.25": 0,
        "1": 0,
        "2": 0
    }

    amount = input 

    for d in DENOMINATIONS[::-1]:
        if amount == 0:
            break 

        div = floor(amount / d) 
        mod = round(amount % d, 2) 

        if div >= 1:
            result[str(d)] = int(div) 
            amount = mod 

    return result


if __name__ == "__main__":
    
    """
    input: amount of required change, given in dollars
    expected: map of denominations, amount of each used
    """
    TESTS = [
        {
            "input": 0.85,
            "expected": {
                "0.01": 0,
                "0.05": 0,
                "0.1": 1,
                "0.25": 3,
                "1": 0,
                "2": 0
            }
        },
        {
            "input": 0.24,
            "expected": {
                "0.01": 4,
                "0.05": 0,
                "0.1": 2,
                "0.25": 0,
                "1": 0,
                "2": 0
            }
        },
        {
            "input": 0.97,
            "expected": {
                "0.01": 2,
                "0.05": 0,
                "0.1": 2,
                "0.25": 3,
                "1": 0,
                "2": 0
            }
        },
        {
            "input": 3.49,
            "expected": {
                "0.01": 4,
                "0.05": 0,
                "0.1": 2,
                "0.25": 1,
                "1": 1,
                "2": 1
            }
        }
    ]

    for test in TESTS:
        result = solution(test.get("input"))
        expected = test.get("expected")

        print("INPUT: {}".format(test.get("input")))

        for _, key in enumerate(expected):
            if result.get(key, -1) == expected[key]:
                print("for {}: {} == {} ".format(key, result[key], expected[key]))
            else: 
                print("FAILED! for {}: expected {} but got {} ".format(key, expected[key], result.get(key, -1)))