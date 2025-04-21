class ListNode:
  def __init__(self,val=None,next=None):
    self.val=val
    self.next=next
class Solution:

  def MiddleNode(self,head):
    slow,fast=head,head

    while fast and fast.next:
      slow=slow.next
      fast=fast.next.next
    return slow
