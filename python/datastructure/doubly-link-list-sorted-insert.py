"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
"""

class Node(object):
    def __init__(self, data = None, next_node = None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

def InsertAtFirst(head, data):
    newNode = Node(data)
    if head is None:
        return newNode

    
    newNode.next = head
    head.prev = newNode
    newNode.prev = None

    head = newNode
    return head
def InsertAtLast(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    current = head
    while current.next:
        current = current.next
    current.next = newNode
    newNode.prev = current
    
    return head


def SortedInsert(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    current = head
    previous = current
    while current and current.data < newNode.data:
        previous = current
        current = current.next

    # If need to insert at last then
    if current is None:
        previous.next = newNode
        newNode.prev = previous
        return head
    # if need to added at first
    if previous.prev is None:
        previous.prev = newNode
        newNode.next = previous
        head = newNode  
        return head
    previous.next = newNode
    newNode.prev = previous
    newNode.next = current
    current.prev = newNode
    return head

def printAsList(head):
    current = head
    str1 = ''
    while current:
        str1 = str1 + str(current.data) + "<->"
        current = current.next

    print(str1)
        
head = InsertAtFirst(None, 2)
head = SortedInsert(head, 1)
head = SortedInsert(head, 4)
head = SortedInsert(head, 3)

printAsList(head)


