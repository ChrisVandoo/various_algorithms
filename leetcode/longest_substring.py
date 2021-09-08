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
        "input": "pwwkew",
        "output": 3
    },
    {
        "input": "",
        "output": 0
    }
]

def solution():
    letters_seen = {}
    sub_str_len = 0  

def test_it():
    for test in TESTS:
            result = solution(test.get("input"))
            if result == test.get("output"):
                print ("SUCESS! {} == {}".format(result, test.get("output")))
            else:
                print("FAIL. {} != {}".format(result, test.get("output")))

if __name__ == "__main__":
    test_it()