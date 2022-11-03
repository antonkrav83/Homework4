a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 4, 6, 8, 9]
c = 0
d = []
for i in range(len(a)):
    if i not in d:
        c += 1
        d.append(i)
print(len(d))