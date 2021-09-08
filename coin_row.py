"""
Problem: 
There is a row of n coins whose values are some positive integers c1, c2, . . . , cn, not necessarily distinct. 
The goal is to pick up the maximum amount of money subject to the constraint that no two coins adjacent in the 
initial row can be picked up.


"""

def solution(coins):
    optimal = []
    optimal.insert(0, 0)
    optimal.insert(1, coins[0])

    for i in range(2, len(coins) + 1):
        optimal.insert(i, max(coins[i - 1] + optimal[i - 2], optimal[i - 1]))
    
    return optimal.pop()


if __name__ == "__main__":
    
    """
    input: an array of "coins"
    expected: the maximum value that can be selected given the parameters defined in the problem statement
    """
    TESTS = [
        {
            "input": [5,1,2,10,6,2],
            "expected": 17
        }
    ]

    for test in TESTS:
        result = solution(test.get("input"))
        if result == test.get("expected"):
            print("PASS! {} == {} ".format(result, test.get("expected")))
        else:
            print("FAILED. Expected {} but got {} ".format(test.get("expected"), result))