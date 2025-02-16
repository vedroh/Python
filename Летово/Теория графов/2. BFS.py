def bfs():
    stack = [s]
    visited[s] = True
    tm[s] = 1
    while len(stack) > 0:
        current = stack.pop(0)
        for v in g[current]:
            if not visited[v]:
                visited[v] = True
                tm[v] = tm[current] + 1
                stack.append(v)
    return max(tm)


n, m, s = map(int, input().split())
s  -=  1
visited = [False] * n  # True, если были в вершине i
tm = [0] * n    # tm[i] - день, когда в деревню i пришла артель коробейников
g = []     # список смежности
for i in range(n):
    g.append([])

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

print(bfs())