from collections import deque

def shortestPath(graph, start, end):
    visited = set()
    queue = deque([(start, 0)])
    
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist+1))
    return -1