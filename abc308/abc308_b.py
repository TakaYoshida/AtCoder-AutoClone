n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))
pricelist = {}
pricelist['any'] = p[0]
for i in range(m):
    pricelist[d[i]] = p[i+1]
# print(pricelist)
ans = 0
for i in range(n):
    if c[i] not in pricelist:
        ans += pricelist['any']
    else:
        ans += pricelist[c[i]]
print(ans)