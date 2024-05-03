n = int(input())
spaces = 0
for row in range(n, 0, -1):
   val = 1
   for space in range(spaces):
       print(" ", end = " ")
   spaces += 1
  
   for num in range(2 * row - 1):
       print(val, end = " ")
       val += 1
   print()
