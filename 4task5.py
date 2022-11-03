number = int(input())
language = []
for i in range(number):
    a = int(input())
    b = set()
    for j in range(a):
        b.add(input())
        language.append(b)
unic = set.union(*language)
intersec = set.intersection(*language)
print(len(intersec), '\n'.join(sorted(intersec)), len(unic), '\n'.join(sorted(unic)), sep='\n')