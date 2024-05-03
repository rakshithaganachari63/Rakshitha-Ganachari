n = int(input())
l = list(map(int, input().split()))


fixThis = n - 1
while fixThis > 0:
   maxIndex = fixThis
   for index in range(fixThis):
       if l[index] > l[maxIndex]:
           maxIndex = index
   if maxIndex != fixThis:
       l[maxIndex], l[fixThis] = l[fixThis], l[maxIndex]
   fixThis -= 1
print(*l)
