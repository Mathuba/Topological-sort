#Uses python3

import sys

def add_edge(graph, vertex1, vertex2):
    if vertex1 in graph:
        graph[vertex1].append(vertex2)
    else:
        graph[vertex1] = vertex2

def dfs(vertex, visited, visited_nodes, graph):
    visited[vertex-1] = True
    for neighbour in graph[vertex]:
        if visited[neighbour-1] is False:
            dfs(neighbour, visited, visited_nodes, graph)
    visited_nodes.append(vertex)    
    
def topsort(adj):
    num_of_nodes = len(graph)
    visited = [False] * num_of_nodes
    ordering = [0] * num_of_nodes
    i = num_of_nodes - 1

    for vertex in graph:
        if visited[vertex-1] is False:
            visited_nodes = []
            dfs(vertex, visited, visited_nodes, graph)
            for node_id in visited_nodes:
                ordering[i] = node_id
                i = i - 1
    return ordering

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    
    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)
    in_order = (topsort(graph))

    for x in in_order:
        print(x, end=' ')

