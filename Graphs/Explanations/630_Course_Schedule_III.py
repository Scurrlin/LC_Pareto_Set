class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        # Step 1: Sort courses by their deadline (earliest deadline first)
        courses.sort(key=lambda c: c[1])
        
        # Max heap to track course durations, current total duration
        A, curr = [], 0
        for dur, ld in courses:

            # Push negative duration (max heap behavior)
            heapq.heappush(A,-dur)

            # Add course duration to current schedule
            curr += dur

            # If we exceed deadline, remove the longest course
            if curr > ld: curr += heapq.heappop(A)

        # Return the total number of courses successfully scheduled    
        return len(A)

# Time Complexity: O(N log N)
# Space Complexity: O(N log N)