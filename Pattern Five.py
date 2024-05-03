n = int(input())
for row in range(n, 0, -1):
   for star in range(row):
       print("*", end = "")
   print()
