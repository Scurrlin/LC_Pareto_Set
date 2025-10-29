class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        maxHeap, total = [], 0
        for duration, lastDay in courses:
            total += duration
            heapq.heappush(maxHeap, -duration)
            if total > lastDay:
                total += heapq.heappop(maxHeap)
        return len(maxHeap)

# Time Complexity: O(N log N)
# Space Complexity: O(N log N)