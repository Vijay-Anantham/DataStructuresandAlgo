class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        kids = [0]*k
        n = len(cookies)
        def recur(i, remain):
            if remain > n-i:
                return float('inf')

            if i == n:
                return max(kids)

            ans = float('inf')
            for j in range(k):
                remain -= int(kids[j] == 0)
                kids[j] += cookies[i]

                ans = min(ans, recur(i+1, remain))

                kids[j] -= cookies[i]
                remain += int(kids[j] == 0)
            
            return ans

        return recur(0, k)