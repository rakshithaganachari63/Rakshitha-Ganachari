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


def insertAtBeginning(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
  
   newNode.next = head
   head.prev = newNode
   head = newNode
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
      
n = int(input())
l = list(map(int, input().split()))
newElement = int(input())
head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = insertAtBeginning(head, newElement)


printLeftToRight(head)
printRightToLeft(head)
