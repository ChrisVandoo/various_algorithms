def twoSum(nums, target):
        my_map = {}
        
        for index, num in enumerate(nums):
            if target - num in my_map:
                return [my_map[target - num], index]
            else:
                my_map[num] = index


if __name__ == "__main__":
    result = twoSum([2,7,11,15], 9)
    print(result)