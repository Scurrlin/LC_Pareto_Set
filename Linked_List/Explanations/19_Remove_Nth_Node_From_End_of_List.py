class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Create a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head

        # First pointer (will move `n+1` steps ahead)
        first = dummy

        # Second pointer (will lag behind)
        second = dummy

        # Move first pointer `n + 1` steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the Nth node from the end
        second.next = second.next.next

        # Return the new head
        return dummy.next

# Time Complexity: O(N)
# Space Complexity: O(1)