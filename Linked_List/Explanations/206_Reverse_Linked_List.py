class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Previous node (initially None, as the last node will point to None)
        prev = None

        # Current node to be processed
        current = head
        
        while current:

            # Store next node before modifying the pointer
            next_node = current.next

            # Reverse pointer to previous node
            current.next = prev

            # Move prev forward
            prev = current

            # Move current forward
            current = next_node
        
        # New head is the last processed node (prev)
        return prev

# Time Complexity: O(N)
# Space Complexity: O(1)