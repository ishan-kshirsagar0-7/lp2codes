import sys

def dijkstra(graph, start):
    visited, distance = set(), {node: sys.maxsize for node in graph}
    distance[start] = 0

    while len(visited) < len(graph):
        min_node = min((node for node in graph if node not in visited), key=distance.get)
        if distance[min_node] == sys.maxsize:
            break
        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            new_dist = distance[min_node] + weight
            distance[neighbor] = min(new_dist, distance[neighbor])

    return distance


if __name__ == '__main__':
    graph = {
        'A': {'B': 6, 'D': 1},
        'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
        'C': {'B': 5, 'E': 5},
        'D': {'A': 1, 'B': 2, 'E': 1},
        'E': {'B': 2, 'C': 5, 'D': 1},
    }
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node + ":")
    for node, distance in shortest_distances.items():
        print("Node:", node, "\tDistance:", distance)