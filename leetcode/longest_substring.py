"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            print(current)
            while s[right] in current:
                current.remove(s[left])
                left += 1

            current.add(s[right])
            longest = max(len(current), longest)

        return longest           

TESTS = [
    {
        "input": "abcabcbb",
        "output": 3
    },
    {
        "input": "bbbbb",
        "output": 1
    },
    {
        "input": "jbpnbwwd",
        "output": 4
    },
    {
        "input": "pwwkew",
        "output": 3
    },
    {
        "input": "",
        "output": 0
    }
]
def test_it():
    for test in TESTS:
            s = Solution()
            result = s.lengthOfLongestSubstring(test.get("input"))
            if result == test.get("output"):
                print ("SUCESS! {} == {}".format(result, test.get("output")))
            else:
                print("FAIL. {} != {}".format(result, test.get("output")))

if __name__ == "__main__":
    test_it()