N, S, M, L = map(int, input().split())
ans = 10**9
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i*6+j*8+k*12 >= N:
                price = S*i+M*j+L*k
                ans = min(ans, price)
print(ans)