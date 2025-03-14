import heapq


def dijkstra_heapq(matrix, start, finish):
    n = len(matrix)
    distances = [101] * n
    distances[start] = 0
    heap = [(0, start)]
    p = [-1] * n

    while heap:
        current_distance, u = heapq.heappop(heap)
        if current_distance > distances[u]:
            continue
        if u == finish:
            break
        for v, length in enumerate(matrix[u]):
            if length > 0:
                if current_distance + length < distances[v]:
                    distances[v] = current_distance + length
                    heapq.heappush(heap, (current_distance + length, v))
                    p[v] = u

    path = []
    current = finish
    while current != -1:
        path.insert(0, current + 1)
        current = p[current]

    return distances[finish], path


def dijkstra(matrix, start, finish):
    size = len(matrix)
    distance = [101] * size
    distance[start] = 0
    visited = [False] * size

    for _ in range(size):
        min_distance = 101
        min_vertex = -1
        for i in range(size):
            if not visited[i] and distance[i] < min_distance:
                min_vertex = i
                min_distance = distance[i]

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        for i in range(size):
            if matrix[min_vertex][i] > 0 and not visited[i] and distance[min_vertex] + matrix[min_vertex][i] < distance[i]:
                    distance[i] = distance[min_vertex] + matrix[min_vertex][i]

    return distance[finish]


n, s, f = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

s -= 1
f -= 1

print(*dijkstra_heapq(matrix, s, f)[1])