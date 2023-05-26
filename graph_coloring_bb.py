def graph_coloring(graph, m):
    vertices = len(graph)
    color_assignment = [-1] * vertices
    color_assignment[0] = 0

    def is_safe(vertex, color):
        for v in range(vertices):
            if graph[vertex][v] and color_assignment[v] == color:
                return False
        return True

    def bound(vertex):
        max_color = max(color_assignment[:vertex]) + 1
        return max_color

    def backtrack(vertex):
        if vertex == vertices:
            return True

        for color in range(m):
            if is_safe(vertex, color):
                color_assignment[vertex] = color
                if bound(vertex) < m:
                    if backtrack(vertex + 1):
                        return True
                color_assignment[vertex] = -1

        return False

    if backtrack(1):
        return color_assignment
    else:
        return None


# canot be colored 
edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [4, 5]]
n = 5

# can be colored 
# edges = [[1, 2], [2, 3], [3, 6], [6, 5], [5, 4], [1, 4]]
# n = 6

graph = [[0] * n for _ in range(n)]
for u, v in edges:
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

m = 3  # Number of colors
color_assignment = graph_coloring(graph, m)

if color_assignment:
    print("Graph coloring possible with at most", m, "colors.")
    print("Color assignment:", color_assignment)
else:
    print("Graph coloring not possible with", m, "colors.")