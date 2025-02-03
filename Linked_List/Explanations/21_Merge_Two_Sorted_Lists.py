class Solution:
    def mergeTwoLists(self, l1, l2):

        # Dummy node to simplify edge cases
        temp = ListNode(0)

        # Pointer for the merged list
        current = temp

        # Merge both lists while both have elements
        while l1 and l2:
            if l1.val <= l2.val:

                # Link current node to l1
                current.next = l1

                # Move l1 forward
                l1 = l1.next
            else:

                # Link current node to l2
                current.next = l2

                # Move l2 forward
                l2 = l2.next

            # Move current forward    
            current = current.next
        
        # If one list is exhausted, attach the remaining part of the other list
        current.next = l1 if l1 else l2
        
        # Return merged list (skip dummy node)
        return temp.next

# Time Complexity: O(N + M)
# Space Complexity: O(1)