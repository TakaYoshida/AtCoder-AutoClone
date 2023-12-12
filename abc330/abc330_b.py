n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append(min(max(l,a[i]),r))
print(*ans)