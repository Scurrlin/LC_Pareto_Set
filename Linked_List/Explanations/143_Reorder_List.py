class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        # Edge case: Empty or single-node list
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list using slow & fast pointers
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second = slow.next

        # Split the list into two halves
        prev = slow.next = None
        while second:

            # Store next node
            temp = second.next

            # Reverse pointer
            second.next = prev

            # Move prev forward
            prev = second

            # Move second forward
            second = temp

        # Step 3: Merge first and second halves alternately
        first, second = head, prev
        while second:

            # Store next nodes
            temp1, temp2 = first.next, second.next

            # Link first half node to second half node
            first.next = second

            # Link second half node to next first half node
            second.next = temp1

            # Move both pointers forward
            first, second = temp1, temp2

# Time Complexity: O(N)
# Space Complexity: O(1)