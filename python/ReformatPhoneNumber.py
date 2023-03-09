import re

class Solution:
    def reformatNumber(self, number: str) -> str:
        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', "1-23-45 6"))
                
    
if __name__ == "__main__":
    s : Solution = Solution()
    
    n : str = "1-23-45 6"
    print(s.reformatNumber(n))
    n : str = "123 4-567"
    print(s.reformatNumber(n))
    n : str = "123 4-5678"
    print(s.reformatNumber(n))