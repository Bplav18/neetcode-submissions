class Solution:
    def search(self, nums: List[int], target: int) -> int:

        r = len(nums)
        i = 0
        while i < r:

                if nums[i] == target:
                    return i
                
                else:
                    i+=1
        
        return -1


     
            
        