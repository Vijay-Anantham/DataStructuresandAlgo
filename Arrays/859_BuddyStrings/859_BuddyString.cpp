class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.length() != goal.length()){return false;}
        int n = s.length();
        // When both strings are same
        // No swaps requried but we check for duplicates so they can be swaped
        if (goal == s){
            set<char> charset(s.begin(), s.end());
            return charset.size() < goal.size();
        }
        
        int i = 0;
        int j = n-1;

        while(i < j && s[i] == goal[i]){
            i++;
        }

        while(j >= 0 && s[j] == goal[j]){
            j--;
        }

        if (i<j){
            swap(s[i], s[j]);
        }

        return s == goal;
        
    }
};
