# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #we need to pick small values while attaching nodes
        p1, p2 = list1 , list2
        tracker = ListNode(0)
        result = tracker
        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    tracker.next = ListNode(p1.val)
                    p1 = p1.next
                else:
                    tracker.next= ListNode(p2.val)
                    p2 = p2.next
            elif p1:
                tracker.next = ListNode(p1.val)
                p1 = p1.next
            elif p2:
                tracker.next= ListNode(p2.val)
                p2 = p2.next
            tracker = tracker.next
        return result.next

            
                

        