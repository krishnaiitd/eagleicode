def MergeLists(headA, headB):
  if headA is None and headB is None:
    return None
  
  if headA is None:
    return headB

  if headB is None:
    return headA
  
  if headA.data < headB.data:
    smallerNode = headA
    smallerNode.next = MergeLists(headA.next, headB)
  else:
    smallerNode = headB
    smallerNode.next = MergeLists(headA, headB.next)
  
  return smallerNode




    current = head
    index = 0
    while index <= positionFromStart:
        current = current.next
        index += 1
        
    return current.data


    Google Interview: Find all contiguous subsequence in a given array of integers, whose sum falls in the given range. Can we do better than O(n^2)?