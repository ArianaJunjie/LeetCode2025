class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        # Every time, the slow pointer move one step forward and the fast       pointer move 2 steps forward
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            # if the fast pointer chase the slow pointer at the back
            if fast == slow:
                return True
    
        return False