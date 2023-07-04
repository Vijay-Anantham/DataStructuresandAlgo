class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # print(bin(2))
        # print(bin(-2))
        # print(bin(-2&2**32-1))

        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & (~twos)
            twos = (twos ^ num) & (~ones)
        
        return ones


        # --------- #
        # ans = 0
        # for i in range(32):
        #     temp = 0
        #     for num in nums:
        #         if num < 0:
        #             num = num & 2**32-1
        #         temp += (num >> i) & 1
            
        #     temp %= 3
        #     ans |= temp << i
        
        # if ans >= 2**31:
        #     ans -= 2**32

        # return ans
            
                

        # -------- #
        # Every element occur 3 times
        # 1112
        # 123412341234
        # 11234
        # THIS CODE IS LINEAR BUT NOT CONSTANT EXTRA SPACE
        # dic = {}
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] not in dic:
        #         dic[nums[i]] = [i]
        #         continue
            
        #     dic[nums[i]].append(i)
        
        # for key, values in dic.items():
        #     if len(values) == 1:
        #         return key