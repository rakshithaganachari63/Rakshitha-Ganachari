n = int(input())
spaces = n - 1
for row in range(1, n + 1):
      
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
  
   val = 1
   for num in range(2 * row - 1):
       print(val, end = "")
       val += 1
   print()
