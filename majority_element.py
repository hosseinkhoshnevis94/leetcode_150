# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Boyer–Moore Voting Algorithm Approach
def maj(nums):
    count = 0
    candidate = None
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
        if(nums[i] == candidate):
            count += 1
        else:
            count -=1
    return candidate
# Time complexity => O(n)
# Space complexity => O(1)     
        
# object (dictionary) approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}  
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1  
            if counts[nums[i]] > len(nums) // 2:  
                return nums[i]
# Time complexity => O(n)
# Space complexity => O(n)     
        

