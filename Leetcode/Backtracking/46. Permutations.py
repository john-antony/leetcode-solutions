class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # res = []

        # if len(nums) == 1:
        #     return [nums[:]]
        
        # for i in range(len(nums)):
        #     n = nums.pop(0)

        #     perms = self.permute(nums)

        #     for perm in perms:
        #         perm.append(n)
        #     res.extend(perms)
        #     nums.append(n)

        # return res

        # recursive DFS backtracking approach
        def dfs(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i, num in enumerate(nums):
                # skip used number
                if used[i]:
                    continue
                
                # add num to permutation, mark as used
                path.append(num)
                used[i] = True
                dfs(path, used, res)
                # remove num from permutation, mark num as unused
                path.pop()
                used[i] = False
        
        res = []
        dfs([], [False] * len(nums), res)
        return res
                