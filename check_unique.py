class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = dict()
        check = []
        for number in arr:
            if res.get(number) is None:
                res[number] = 0
            else:
                res[number] += 1
        
        for key, val in res.items():
            if val not in check:
                check.append(val)
            else:
                return False
        
        return True