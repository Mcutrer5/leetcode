class Solution:
    def __init__(self, s) -> None:
        self.s = s
    def lengthOfLongestSubstring(self):
        final = ""
        temp = ""
        oldChar = ""
        count = 0
        highest = 0
        for character in self.s:
            if character not in temp:
                temp += character
                count += 1
                if count > highest:
                    highest = count
                    final = temp
            else:
                temp = ""
                count = 0
            
        print("The answer is ", final, " with a length of ", highest, ".")
        return highest
    
if __name__ == '__main__':
    print(Solution("abcabcbb").lengthOfLongestSubstring())
    print(Solution("bbbbb").lengthOfLongestSubstring())
    print(Solution("pwwkew").lengthOfLongestSubstring())