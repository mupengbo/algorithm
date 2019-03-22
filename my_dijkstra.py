import heapq
import math


def init_distance(graph, start_node):
    distance = {}
    for node in graph.keys():
        distance[node] = math.inf
    distance[start_node] = 0
    return distance


def dijkstra(graph, start_node):
    pqueue = []
    heapq.heappush(pqueue, (0, start_node))
    seen = set()
    seen.add(start_node)
    distance = init_distance(graph, start_node)
    parent = {start_node: None}

    while pqueue:
        pair = heapq.heappop(pqueue)
        vertex = pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in seen:
                heapq.heappush(pqueue, (graph[vertex][node], node))
                if distance[node] > distance[vertex] + graph[vertex][node]:
                    parent[node] = vertex
                    distance[node] = distance[vertex] + graph[vertex][node]
    return parent, distance


if __name__ == '__main__':
    graph = {
        'A': {'B': 5, 'C': 1},
        'B': {'A': 5, 'C': 2, 'D': 1},
        'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
        'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
        'E': {'C': 8, 'D': 3},
        'F': {'D': 6}
    }

    parent, distance = dijkstra(graph, 'A')
    print('parent: ', parent)
    print('distance: ', distance)
