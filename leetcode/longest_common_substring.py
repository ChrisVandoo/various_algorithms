"""
Write a function to find the longest common prefix string amongst an array of strs.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strs.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

def solution(strs: list[str]) -> str:
    i = 0
    common_prefix = ""
    loop = True
    while loop:
        for str in strs:
            if i >= len(str) or str[i] != strs[0][i]:
                loop = False
                break
        
        common_prefix = strs[0][:i]
        i += 1
    
    return common_prefix 

TESTS = [
    {
        "input": ["flower","flow","flight"],
        "output": "fl"
    },
    {
        "input": ["dog","racecar","car"],
        "output": ""
    },
]
def test_it():
    for test in TESTS:
            result = solution(test.get("input"))
            if result == test.get("output"):
                print ("SUCESS! {} == {}".format(result, test.get("output")))
            else:
                print("FAIL. {} != {}".format(result, test.get("output")))

if __name__ == "__main__":
    test_it()