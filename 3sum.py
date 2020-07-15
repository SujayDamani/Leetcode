class Solution:
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        nums.sort()
        print(nums)
        for i in range(0,len(nums)-1):
            if i>0:
                if nums[i]==nums[i-1]:
                    continue
            right = len(nums)-1
            left = i+1
            print(right,left)
            while True:
                if left>=right:
                    break
                sum_val=nums[i]+nums[left]+nums[right]
                if sum_val==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                    while nums[left]==nums[left-1] and left<right:
                        left=left+1
                    while nums[right]==nums[right+1] and right>left:
                        right=right-1
                elif sum_val>0:
                    right=right-1
                    while nums[right]==nums[right+1] and right>left:
                        right=right-1
                        
                elif sum_val<0:
                    left=left+1
                    while nums[left]==nums[left-1] and left<right:
                        left=left+1
                
                    
        
        return ans

    
