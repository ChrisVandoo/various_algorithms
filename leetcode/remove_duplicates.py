"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
"""

def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    
    count = 1
    checked = 0
    while count < len(nums) and nums[count - 1] <= nums[count] and checked <= len(nums):
        checked += 1
        if nums[count - 1] == nums[count]:
            num = nums.pop(count)
            nums.append(num)
        else:
            count += 1

    return count

TESTS = [
    {
        "input": [1,1,2],
        "output": 2
    },
    {
        "input": [0,0,1,1,1,2,2,3,3,4],
        "output": 5
    },
]

def test_it():
    for test in TESTS:
        result = removeDuplicates(test["input"])
        if result == test.get("output"):
            print ("SUCESS! {} == {}".format(result, test.get("output")))
        else:
            print("FAIL. {} != {}".format(result, test.get("output")))

if __name__ == "__main__":
    test_it()