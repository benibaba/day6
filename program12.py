from itertools import takewhile
n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = input("Enter element : ")
    arr.append(d)

res = ''.join(c[0] for c in takewhile(lambda x:all(x[0] == y for y in x), zip(*arr)))

print("Longest prefix: ",res)
