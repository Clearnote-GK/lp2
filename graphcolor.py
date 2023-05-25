#!/usr/bin/env python
# coding: utf-8

# In[4]:


def graph_coloring(graph, colors):
    num_vertices = len(graph)
    solution = [-1] * num_vertices

    def is_safe(vertex, color):
        for neighbor in range(num_vertices):
            if graph[vertex][neighbor] == 1 and solution[neighbor] == color:
                return False
        return True

    def solve(vertex):
        if vertex == num_vertices:
            return True

        for color in range(colors):
            if is_safe(vertex, color):
                solution[vertex] = color
                if solve(vertex + 1):
                    return True
                solution[vertex] = -1

        return False

    if solve(0):
        return solution
    else:
        return []

# Test the algorithm
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
colors = 3  # Number of colors to be used
solution = graph_coloring(graph, colors)

if solution:
    print("Graph coloring solution found:")
    for vertex, color in enumerate(solution):
        print(f"Vertex {vertex+1}: Color {color}")
else:
    print("No solution found for graph coloring problem")


# In[ ]:




