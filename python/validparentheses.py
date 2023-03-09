# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s:str) -> bool:
        valid_characters = ['(','{','[' ]
        for character in s:
            if character in valid_characters:
                match(character):
                    case('('):
                        end_char = ")"
                    case('{'):
                        end_char = "}"
                    case('['):
                        end_char = "]"
                for char in s:
                    if char in end_char:
                        return True
        return False
                
        
def main():
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    
if __name__ == "__main__":
    main()