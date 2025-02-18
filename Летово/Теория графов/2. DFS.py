def dfs(start):
    Visited[start] = True
    print(start)
    for v in V[start]:
        if not Visited[v]:
            dfs(v)


n, m, s = map(int, input().split())
Visited = [False]*(n+1)
V = [set() for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    V[u].add(v)
    V[v].add(u)

dfs(s)
