import math


def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([math.inf if x == -1 else x for x in list(map(int, input().split()))])

distance = floyd_warshall(matrix)

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    print(distance[a - 1][b - 1] if distance[a - 1][b - 1] != math.inf else "Imp")
