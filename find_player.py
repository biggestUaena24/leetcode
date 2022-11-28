class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player = {}
        res = [[],[]]
        #record loss
        for p in matches:
            if p[0] not in player.keys():
                player[p[0]] = 0
            
            if p[1] not in player.keys():
                player[p[1]] = 1
            else:
                player[p[1]] += 1
        
        for key, val in player.items():
            if val == 0:
                res[0].append(key)
            elif val == 1:
                res[1].append(key)

        res[0].sort()
        res[1].sort()
        return res