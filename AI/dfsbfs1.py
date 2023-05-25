#!/usr/bin/env python
# coding: utf-8

# In[3]:


def dfs(visited,graph,node):
    if node not in visited:
        print(node,end= " ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)
            
            
def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)
    
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
def main():
    visited1=set()
    visited2=set()
    queue=[]
    n=int(input("Enter No.Of Nodes : "))
    graph={}
    
    for i in range(1,n+1):
        edges=int(input("Enter NO. of edges for node {}:".format(i)))
        graph[i]=[]
        for j in range(1,edges+1):
            node=int(input("Enter edge {} for node {}:".format(j,i)))
            graph[i].append(node)
            
    print("DFS: ")
    dfs(visited1,graph,1)
    print()
    print("BFS: ")
    bfs(visited2,graph,1,queue)

if __name__ == "__main__":
    main()


# In[ ]:




