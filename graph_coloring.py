def is_graph_colorable(graph, node, visited, color, c):
    visited[node] = 1
    color[node] = c
    for child in graph[node]:
        if not visited[child]:
            if not is_graph_colorable(graph, child, visited, color, c ^ 1):
                return False
        elif color[node] == color[child]:
            return False
    return True

# canot be colored 
edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [4, 5]]
n = 5

# can be colored 
# edges = [[1, 2], [2, 3], [3, 6], [6, 5], [5, 4], [1, 4]]
# n = 6

graph = {}
visited = {}
color = {}

for u, v in edges:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
    visited[u] = 0
    visited[v] = 0
    color[u] = None
    color[v] = None

temp = is_graph_colorable(graph, 1, visited, color, 0)
if temp:
    print("The graph is colorable.")
else:
    print("The graph is not colorable.")