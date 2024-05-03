class Box:
   def __init__(self, data):
       self.data = data
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
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
      
def deleteHeadNode(head):
   if head == None or head.next == None:
       return None
  
   head = head.next
   return head
  
n = int(input())
l = list(map(int, input().split()))


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)


head = deleteHeadNode(head)


printLeftToRight(head)
