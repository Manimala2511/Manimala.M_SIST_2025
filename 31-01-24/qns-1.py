#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

 

#Example 1:

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]
#Example 2:

#Input: nums = [-1,1,0,-3,3]
#Output: [0,0,9,0,0]
 

#Constraints:

#2 <= nums.length <= 105
#-30 <= nums[i] <= 30
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


#Python_Product of Array Except Self


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix= [1] * n
        suffix= [1] * n
        t = [1] * n

        for i in range(1, n):
           prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
           suffix[i] = suffix[i + 1] * nums[i + 1]
        for i in range(n):
           t[i] = prefix[i] * suffix[i]

        return t

c=Solution()
nums1 = [1, 2, 3, 4]
print(c.productExceptSelf(nums1))  

nums2 = [-1, 1, 0, -3, 3]
print(c.productExceptSelf(nums2))  
