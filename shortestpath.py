#!/usr/bin/env python
# coding: utf-8

# ## 

# In[53]:


from heapq import *

def dijkstra(graph, start):
    distances = {}  
    visited = set()  
    bag = []  

    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0

    heappush(bag, (distances[start], start))

    while bag:
        current_dist, current_node = heappop(bag)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, edge_weight in graph[current_node]:
            distance = current_dist + edge_weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(bag, (distance, neighbor))

    return distances

graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 1), ('E', 6)],
    'C': [('B', 1), ('D', 2)],
    'D': [('E', 4)],
    'E': []
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

for node, distance in shortest_distances.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")


# In[ ]:




