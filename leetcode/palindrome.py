TESTS = [
    {
        "input": "a",
        "output": "a"
    },
    {
        "input": "babdd",
        "output": "bab"
    },
    {
        "input": "someoonooasdf",
        "output": "oonoo"
    }
]

def longest_palindrome_take_1(s):
    sub_str = len(s)
    
    while sub_str > 0:
        left = 0
        right = sub_str
        while right <= len(s):
            s_invert = s[left:right]
            # print("s:{} s-1:{}".format(s[left:right], s_invert[::-1]))
            if s[left:right] == s_invert[::-1]:
                return s[left:right]
            left+= 1
            right+= 1
        
        sub_str-=1

def improved_answer(s):
    pass

def test_it():
    for test in TESTS:
        result = improved_answer(test.get("input"))
        if result == test.get("output"):
            print ("SUCESS! {} == {}".format(result, test.get("output")))
        else:
            print("FAIL. {} != {}".format(result, test.get("output")))


if __name__ == "__main__":
    test_it()
