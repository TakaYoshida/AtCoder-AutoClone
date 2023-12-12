M, D = map(int, input().split())
y, m, d = map(int, input().split())
ans_y, ans_m, ans_d = y, m, d+1
if ans_d > D:
    ans_d = 1
    ans_m += 1
    if ans_m > M:
        ans_m = 1
        ans_y += 1
print(ans_y, ans_m, ans_d)