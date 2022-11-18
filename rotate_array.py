class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replicate = [num for num in nums]
        index = len(nums) - (k % len(nums))

        for i in range(len(nums)):
            print(index % len(nums))
            nums[i] = replicate[index % len(nums)]
            index += 1
        return