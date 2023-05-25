from heapq import heappop, heappush, heapify

def prim(graph):
    start_vertex = list(graph.keys())[0]
    mst = []
    visited = set([start_vertex])
    edges = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapify(edges)

    while edges:
        weight, u, v = heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heappush(edges, (weight, v, neighbor))

    return mst

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

minimum_spanning_tree = prim(graph)
for edge in minimum_spanning_tree:
    u, v, weight = edge
    print(f'{u} -- {v}: {weight}')