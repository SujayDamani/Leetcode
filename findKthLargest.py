class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        print(nums)
        if k==1:
            return nums[len(nums)-1]
        
        return nums[len(nums)-k]
            