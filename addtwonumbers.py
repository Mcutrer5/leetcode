# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    
    def addTwoNumbers(self):
        # reverse list 
        l1 = list(reversed(self.l1))
        l2 = list(reversed(self.l2))
        temp1 = ""
        temp2 = ""
        
        for i in l1 or []:
            temp1 += str(i)
        for j in l2 or []:
            temp2 += str(j)
            
        total = int(temp1) + int(temp2)
        total = str(total)
        final = []
        for char in total:
            final.append(char)
        return list(reversed(final))
                
            
    
if __name__ == "__main__":
    test1 = Solution([2,4,3], [5,6,4])
    test2 = Solution([0],[0])
    test3 = Solution([9,9,9,9,9,9,9], [9,9,9,9])
    
    print("Test 1: ", test1.addTwoNumbers())
    print("Test 2: ", test2.addTwoNumbers())
    print("Test 3: ", test3.addTwoNumbers())