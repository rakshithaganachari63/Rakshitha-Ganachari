n = int(input())
l = list(map(int, input().split()))


for index in range(1, n):
   position = index - 1
   temp = l[index]
   while position >= 0:
       if l[position] > temp:
           l[position + 1] = l[position]
       else:
           break
       position -= 1
   l[position + 1] = temp
          


print(*l)
