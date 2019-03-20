#!/bin/env python3
# BFS --> Breadth First Search
# DFS --> Depth First Search

#          B ---- D
#        / |     /| \
#       /  |    / |  \
#     A    |   /  |   F
#       \  |  /   |
#        \ | /    |
#          C ---- E


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D'],
}


def bfs(graph, start_node):
    queue = []
    queue.append(start_node)
    seen = set()
    seen.add(start_node)
    while queue:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)

def dfs(graph, start_node):
    stack = []
    stack.append(start_node)
    seen = set()
    seen.add(start_node)
    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)


if __name__ == '__main__':
    print('---------- 广度优先---------')
    bfs(graph, 'A')
    print('---------- 深度优先---------')
    dfs(graph, 'A')
