n = int(input())


stars = 2 * n - 1
spaces = 0


for row in range(n):
   for space in range(spaces):
       print(" ", end = " ")
   spaces += 1
  
   for star in range(stars):
       print("*", end = " ")
   stars -= 2
   print()
  
stars += 4
spaces -= 2
for row in range(1, n):
   for space in range(spaces):
       print(" ", end = " ")
   spaces -= 1
  
   for star in range(stars):
       print("*", end = " ")
   stars += 2
   print()

