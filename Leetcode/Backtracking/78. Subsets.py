class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        subset = [] 

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # if nums[i] is included in decision
            subset.append(nums[i])
            dfs(i + 1)

            # decision to not include nums[i] get rid of empty set
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

            