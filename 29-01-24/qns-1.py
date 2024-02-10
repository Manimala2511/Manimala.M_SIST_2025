"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

#logic
class Solution:
    def twoSum(self, nums, target):
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
               
                return [num_indices[complement], i]

            num_indices[num] = i

        return []


nums1 = [2, 7, 11, 15]
target1 = 9
sol = Solution()
print(sol.twoSum(nums1, target1))  

nums2 = [3, 2, 4]
target2 = 6
print(sol.twoSum(nums2, target2))  

nums3 = [3, 3]
target3 = 6
print(sol.twoSum(nums3, target3))  
