"""
Just to test stuff.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):

    if not head or not head.next:
        return head
    
    oddll = head
    evenll = head.next
    newhead = oddll #the head of the odd list, which will be the head of entire ll
    split = evenll #the head of the even list
    tail = oddll
    while evenll and oddll:
        oddll.next = evenll.next
        evenll.next = None
        if oddll.next:
            evenll.next = oddll.next
            tail = oddll.next
        oddll, evenll = oddll.next, evenll.next

    tail.next = split
    return newhead

ll= ListNode(1)
ll.next = ListNode(2)
oddEvenList(ll)
