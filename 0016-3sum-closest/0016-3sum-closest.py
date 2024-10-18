class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
            
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    left += 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                elif current_sum > target:
                    right -= 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                else:
                    return current_sum
        return closest_sum