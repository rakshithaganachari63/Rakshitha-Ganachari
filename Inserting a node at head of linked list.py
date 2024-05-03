def insertNodeAtHead(llist, data):
   newNode = SinglyLinkedListNode(data)
   if llist == None:
       return newNode
   newNode.next = llist
   return newNode
