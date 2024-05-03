def findPosition(l, left, right):
   pivot = l[right]
   position = left
   index = left
  
   while index < right:
       if l[index] < pivot:
           l[position], l[index] = l[index], l[position]
           position += 1
       index += 1
      
   l[position], l[right] = l[right], l[position]
   return position
  


def divideIt(l, left, right):
   if left >= right:
       return
  
   position = findPosition(l, left, right)
   divideIt(l, left, position - 1)
   divideIt(l, position + 1, right)


def quickSort(l):
   divideIt(l, 0, len(l) - 1)


n = int(input())
l = list(map(int, input().split()))


quickSort(l)
      
print(*l)

