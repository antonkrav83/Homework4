dict={}
for i in range(int(input())):
    country, *cities = input().split()
    for j in cities:
        dict[j]=country
for i in range(int(input())):
    print(dict[input()])
