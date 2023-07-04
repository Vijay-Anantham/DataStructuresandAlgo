class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums.size();
        int ones = 0;
        int twos = 0;

        for (auto num : nums){
            ones = (ones ^ num) & (~twos);
            twos = (twos ^ num) & (~ones);
        }

        return ones;
    }
};