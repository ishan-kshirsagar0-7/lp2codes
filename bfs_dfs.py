import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

bfsvisited = []
start = 'A'

bfsqueue = []

def bfs(visited, graph, start):
    visited.append(start)
    bfsqueue.append(start)
    final = []

    while bfsqueue:
        m = bfsqueue.pop(0)
        final.append(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                bfsqueue.append(neighbour)
        
    return final

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print(f"The BFS Order for the given graph is: {bfs(bfsvisited, graph, start)}")
print("The DFS order for the given graph is: ")
dfs(graph, start)

G = nx.Graph(graph)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray')

plt.title("Graph")
plt.axis('off')
plt.show()