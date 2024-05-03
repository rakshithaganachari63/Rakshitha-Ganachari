class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
def deleteTailNode(head):
   if head == None or head.next == None:
       return None
  
   prev = None
   curr = head
   while curr.next != None:
       prev = curr
       curr = curr.next
      
   prev.next = None
   return head
  
n = int(input())
l = list(map(int, input().split()))


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = deleteTailNode(head)


printLeftToRight(head)
printRightToLeft(head)
