n = int(input())
spaces = n - 1
for row in range(1, n + 1):
      
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
  
   for col in range(1, row + 1):
       print(col, end = "")
   print()
