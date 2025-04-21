class ListNode:
  def __init__(self,val=None,next=None):
    self.val=val
    self.next=next
class Solution:
  def detectRemove(self,head):
    hasCycle=False
    slow,fast=head,head
    while fast and fast.next:
      slow=slow.next
      fast=fast.next.next
      if slow==fast:
        hasCycle=True
        break

    prev=None
    slow=head
    while slow!=fast:
      prev=fast
      slow=slow.next
      fast=fast.next.next

    prev.next=None
    return head
