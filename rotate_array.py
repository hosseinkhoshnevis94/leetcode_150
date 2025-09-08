# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr,start,end):
            while(start < end):
                arr[start],arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n #in the case if k is greater than n
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)

# Time complexity => O(n)
# Space complexity => O(1)     
        