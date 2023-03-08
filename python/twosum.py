class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
class test_cases():
    def test_one(self):
        return Solution().twoSum([2, 7, 11, 15], 9)
    def test_two(self):
        return Solution().twoSum([3, 2, 4], 6)
    def test_three(self):
        return Solution().twoSum([3, 3], 6)
        
if __name__ == "__main__":
    test1 = test_cases().test_one()
    test2 = test_cases().test_two()
    test3 = test_cases().test_three()
    
    print(test1)
    print(test2)
    print(test3)
