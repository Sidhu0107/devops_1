def tsp(graph, v, start, path, cost):
    if len(path) == len(graph):
        return cost + graph[v][start], path + [start]  # Return to start
    return min((tsp(graph, nv, start, path + [nv], cost + graph[v][nv]) 
               for nv in graph if nv not in path), key=lambda x: x[0])
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
cost, path = tsp(graph, 'A', 'A', ['A'], 0)
print("Optimal Path:", " -> ".join(path))
print("Minimum Cost:", cost)