n = int(input())
spaces = 0


for i in range(n, 0, -1):
   for j in range(spaces):
       print(" ", end = " ")
   spaces += 1
   for j in range(2 * i - 1):
       print("*", end = " ")
   print()
