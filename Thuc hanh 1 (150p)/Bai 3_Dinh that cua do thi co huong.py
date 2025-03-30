
def check(ke, u, v, e, n):
    q = [u]
    visited = [0] * (n + 1)
    visited[u] = 1
    while q:
        x = q.pop()
        if x == v:
            return False
        for i in ke[x]:
            if visited[i] == 0 and  i != e:
                q.append(i)
                visited[i] = 1
    return True

for _ in range(int(input())):
    n, m, u, v = map(int, input().split())
    ke ={x: [] for x in range(1, n + 1)}

    for i in range(m):
        x, y = map(int, input().split())
        ke[x].append(y)
    cnt = 0
    for i in range(n+1):
        if i != u and i != v and check(ke, u, v,i,n):
            cnt += 1
    print(cnt)

