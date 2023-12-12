K, G, M = map(int, input().split())
Glass, Magcup = 0, 0
for i in range(K):
    if Glass == G:
        Glass = 0
    elif Magcup == 0:
        Magcup = M
    else:
        move = min(Magcup,G-Glass)
        Glass += move
        Magcup -= move
print(Glass, Magcup)