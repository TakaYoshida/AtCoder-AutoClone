a = ['a','b','c','d','e','f','g','h']
pos_a, pos_n = 0, 0
for i in range(8):
    str = list(input())
    if '*' in str:
        pos_n = abs(i-8)
        for j in range(8):
            if str[j] == '*':
                pos_a = j
print('{}{}'.format(a[pos_a], pos_n))