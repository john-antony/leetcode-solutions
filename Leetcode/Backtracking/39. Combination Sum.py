class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total > target or i >= len(candidates):
                return
            if total == target:
                res.append(curr.copy())
                return
            
            # if we choose to include candidates[i]
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            # we choose not to include candidates[i]

            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)

        return res
            