class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        
        return False
        
        
        '''nums.sort()
        for i in nums:
            if i == (len(nums) - 1):
                break
            if nums[i] == nums[i+1]:
                return True
            
        return False'''
