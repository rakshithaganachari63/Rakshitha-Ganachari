n = int(input())
spaces = 0
for i in range(n, 0, -1):
  for j in range(spaces):
      print(" ",  end = " ")
  spaces += 1
   letter = 65
  for j in range(i):
      print(chr(letter), end = " ")
      letter += 1
  print()
