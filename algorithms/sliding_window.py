

def maximize(input: list[int], count: int) -> int:
    # error if count is bigger than list
    if count > len(input):
        return 0

    # initialize first "count"
    total = 0
    for i in range(count):
        total += input[i]

    # start right pointer at count
    max = total
    left = 0
    for right in range(count, len(input)):
        total = total + input[right] - input[left]
        if total > max:
            max = total
        left += 1
        
        
    return max

if __name__ == "__main__":
    input = [2, 8, 6, -2, 4, -3, -10, 11, 15, 1, 2, 2, -5, 6, -10]
    print(maximize(input, 5))