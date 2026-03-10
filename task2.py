
n = 5


g = [
    [0,1],
    [1],
    [3,2],
    [2,3],
    [3,4]
]


match = [-1]*n

#алгоритм поиска в глубину
def dfs(v, used):
    if used[v]:
        return False
    used[v] = True
    for to in g[v]:
        if match[to] == -1 or dfs(match[to], used):
            match[to] = v
            return True
    return False


for v in range(n):
    used = [False]*n
    dfs(v, used)


for y in range(n):
    if match[y] != -1:
        print(f"x{match[y]+1} - y{y+1}")
