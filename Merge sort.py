def mergeThese(l, left, mid, right):
   temp = []
   index1 = left
   index2 = mid + 1
  
   while index1 <= mid and index2 <= right:
       if l[index1] > l[index2]:
           temp.append(l[index2])
           index2 += 1
       else:
           temp.append(l[index1])
           index1 += 1
          
   while index1 <= mid:
       temp.append(l[index1])
       index1 += 1
      
   while index2 <= right:
       temp.append(l[index2])
       index2 += 1
      
   position = 0
   for index in range(left, right + 1):
       l[index] = temp[position]
       position += 1


def divideIt(l, left, right):
   if left == right:
       return
  
   mid = (left + right) // 2
   divideIt(l, left, mid)
   divideIt(l, mid + 1, right)
   mergeThese(l, left, mid, right)


def mergeSort(l):
   divideIt(l, 0, len(l) - 1)


n = int(input())
l = list(map(int, input().split()))


mergeSort(l)
          


print(*l)

