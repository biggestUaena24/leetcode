class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        merged = []
        res = 0
        #making a merged list of numbers by two pointers
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                merged.append(nums1.pop(0))
            elif nums2[0] < nums1[0]:
                merged.append(nums2.pop(0))
            elif nums1[0] == nums2[0]:
                merged.append(nums1.pop(0))
        merged += nums2
        merged += nums1
        # try to find the median of the array
        if len(merged) % 2 == 1:
            res = merged[len(merged) // 2]
        elif len(merged) % 2 == 0:
            temp1 = merged[len(merged) // 2]
            temp2 = merged[len(merged) // 2 - 1]
            res = (temp1+temp2) / 2

        return float(res)