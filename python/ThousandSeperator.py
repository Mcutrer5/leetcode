class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str : str = str(n)
        result : str = "" 
        counter : int = 0
        if len(n_str) > 3:
            for character in reversed(n_str):
                if counter >= 3:
                    result += "," + character  
                    if len(result) > 3:                  
                        counter = 1
                    else:
                        counter = 0
                else: 
                    result += character
                    counter += 1
            
            return result[::-1]
        else:
            return n
            
        
def main():
    s : Solution = Solution()
    n : int = 987
    print(s.thousandSeparator(n))
    n : int = 1234
    print(s.thousandSeparator(n))
    n : int = 123456789
    print(s.thousandSeparator(n))
    n : int = 53937897432564198196
    print(s.thousandSeparator(n))

if __name__ == "__main__":
    main()