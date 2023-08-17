class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here

        if not n:
            return True
        
        adjacencyList = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)
        
        visited = set()

        def dfs(i, prevN):
            if i in visited:
                return False
            
            visited.add(i)

            for j in adjacencyList[i]:
                if j == prevN:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        # ensures the nodes are connected
        return dfs(0, -1) and n == len(visited)