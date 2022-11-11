class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = set(nums)
        index = 0

        while len(nums)!= len(res):
            if nums[index] == nums[index + 1]:
                nums.pop(index + 1)
            else:
                index += 1
        
        return len(res)