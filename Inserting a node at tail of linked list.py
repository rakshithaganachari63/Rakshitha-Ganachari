def insertNodeAtTail(head, data):
   newNode = SinglyLinkedListNode(data)
   if head == None:
       return newNode
  
   tail = head
   while tail.next != None:
       tail = tail.next
   tail.next = newNode
   return head
