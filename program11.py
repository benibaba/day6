a = list(map(int, input("Enter the  elements: ").split()))
a.sort(reverse = True)
print(a[0] *a[1] * a[2], "is obtained by multiplying " 
      + str(a[0]) + "," + str(a[1]) + "," + str(a[2]))
