<<<<<<< HEAD
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(goal)
        if len(s) != n: return False
        dic = {}
        haspair = False
        for i in range(n):
            if goal[i] not in dic:
                dic[goal[i]] = [i]
                continue
            haspair |= True
            dic[goal[i]].append(i)
        misses = -1
        replace = False
        for j in range(n):
            if s[j] != goal[j]:
                if misses == -1:
                    misses = [s[j], goal[j]]
                else:
                    if replace: return False
                    if misses[0] != goal[j]: return False
                    if misses[1] != s[j]: return False
                    replace = True
                    misses = -1

        print(haspair, misses, replace)
        ans = (haspair | replace)
        if misses != -1:
            ans &= (misses[0] == misses[1])

        return ans

            

=======
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(goal)
        if len(s) != n: return False
        dic = {}
        haspair = False
        for i in range(n):
            if goal[i] not in dic:
                dic[goal[i]] = [i]
                continue
            haspair |= True
            dic[goal[i]].append(i)
        misses = -1
        replace = False
        for j in range(n):
            if s[j] != goal[j]:
                if misses == -1:
                    misses = [s[j], goal[j]]
                else:
                    if replace: return False
                    if misses[0] != goal[j]: return False
                    if misses[1] != s[j]: return False
                    replace = True
                    misses = -1

        print(haspair, misses, replace)
        ans = (haspair | replace)
        if misses != -1:
            ans &= (misses[0] == misses[1])

        return ans

            

>>>>>>> 301a30447c97bc9ef626248608381833da126271
