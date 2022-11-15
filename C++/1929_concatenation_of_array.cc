// 1929. Concatenation of Array - Easy

// Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

// Specifically, ans is the concatenation of two nums arrays.

// Return the array ans.w


class Solution {
 public:
   vector<int> getConcatenation(vector<int> &nums)
   {
     const int n = nums.size();

     for (int i = 0; i < n; ++i)
       nums.push_back(nums[i]);

     return nums;
  }
};