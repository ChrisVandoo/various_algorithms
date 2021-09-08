TESTS = [
    {
        "l1": [2,4,3],
        "l2": [5,6,4],
        "output": [7,0,8]
    },
    {
        "l1": [9,9,9,9,9,9,9],
        "l2": [9,9,9,9],
        "output": [8,9,9,9,0,0,0,1]
    },
    {
        "l1": [0],
        "l2": [0],
        "output": [0]
    }
]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def solution(l1, l2):
    ans = []
    carry_one = 0
    while l1.next != None and l2.next != None:
        result = l1.val + l2.val + carry_one
        if result > 9:
            carry_one = 1
            result = result % 10
        else:
            carry_one = 0

        ans.append(result)
        l1 = l1.next
        l2 = l2.next

    if l1.next != None:
        while l1.next != None:
            if carry_one != 0:
                if l1.val + carry_one > 9:
                    ans.append(0)
                    carry_one = 1
                else:  
                    ans.append(l1.val + carry_one)
                    carry_one = 0
            else:
                ans.append(l1.val)

            l1 = l1.next

        if carry_one == 1:
            ans.append(1)
    
    if l2.next != None:
        while l2.next != None:
            if carry_one != 0:
                if l1.val + carry_one > 9:
                    ans.append(0)
                    carry_one = 1
                else: 
                    ans.append(l2.val + carry_one)
                    carry_one = 0
            else:
                ans.append(l2.val)

            l2 = l2.next

        if carry_one == 1:
            ans.append(1)

    return ans 



def init_list(nums):
    curr = ListNode()
    head = curr 

    for num in nums:
        curr.val = num 
        curr.next = ListNode()
        curr = curr.next
    
    return head 

def test_it():

    for test in TESTS:
        result = solution(init_list(test.get("l1")), init_list(test.get("l2")))
        if result == test.get("output"):
            print ("SUCESS! {} == {}".format(result, test.get("output")))
        else:
            print("FAIL. {} != {}".format(result, test.get("output")))


if __name__ == "__main__":
    test_it()