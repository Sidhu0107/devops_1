from collections import deque

graph={'A':["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["F"],"F":[]}

def bfs(graph,start):
    visited,queue={start},deque([start])
    print("BFS Traversal:",end=" ")
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbor in graph[node]:
           if neighbor not in visited:
                 visited.add(neighbor)
                 queue.append(neighbor)
bfs(graph,"A")