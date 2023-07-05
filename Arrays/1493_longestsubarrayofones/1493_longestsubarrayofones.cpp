class Solution {
public:
    int longestSubarray(vector<int>& nums) {

        int start, longest_window, zeros;
        start = zeros = longest_window = 0;
        for (int i=0; i<nums.size(); i++){
            zeros += (nums[i] == 0);
            if (zeros > 1){
                zeros -= (nums[start] == 0);
                start++;
            }

            longest_window = max(longest_window, i-start);
        }
        return longest_window;
    }
};