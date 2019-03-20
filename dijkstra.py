#!/bin/env python3
# Dijkstra 加权图的最短路径算法

import heapq
import math


graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6},
}


def init_distance(graph, start_node):
    distance = {s: 0}
    for vertex in graph:
        if vertex != start_node


def dijkstra(graph, start_node):
    pqueue = []
    heapq.heappush(pqueue, (0, start_node))
    seen = set()
    seen.add(start_node)
    parent = {s: None}
    distance = {s: 0}

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in seen:
                if dist + graph[vertex][node] < distance[node]:
                    heapq.heappush(pqueue, (dist + graph[vertex][node], node))
                    parent[node]


if __name__ == '__main__':
    dijkstra(graph, 'A')
