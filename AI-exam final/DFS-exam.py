graph={'A':["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["F"],"F":[]}

def dfs(graph,start):
    visited,stack={start},[start]
    print("DFS Traversal:",end=" ")
    while stack:
        node=stack.pop()
        print(node,end=" ")
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
dfs(graph,"A")