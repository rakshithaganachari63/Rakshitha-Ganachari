n = int(input())
spaces = 0


for row in range(n):
   for space in range(spaces):
       print(" ", end = "")
   for star in range(n):
       print("*", end = "")
   spaces += 1
   print()
