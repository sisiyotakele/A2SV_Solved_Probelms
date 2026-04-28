class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def bfs (graph):
            target = len(graph) - 1 
            res = []
            queue = deque ([[0]])

            while queue:
                path = queue.popleft()
                node = path[-1]
                if node == target :
                    res.append(path)
                else:
                    for neighbour in graph[node]:
                        new_path = path + [neighbour]
                        queue.append(new_path)
            return res
        return bfs(graph)