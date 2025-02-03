import collections

class LRUCache:
    def __init__(self, capacity: int):

        # Set cache capacity
        self.capacity = capacity

        # OrderedDict maintains insertion order
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:

        # If key is not found, return -1
        if key not in self.dic:
            return -1

        # Move key to end to mark as recently used
        self.dic.move_to_end(key)

        # Return the value
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:

            # Move existing key to end to mark as recently used
            self.dic.move_to_end(key)

        # Insert or update key-value pair
        self.dic[key] = value

        # If cache exceeds capacity, remove the least recently used item
        if len(self.dic) > self.capacity:

            # Remove the first (least recently used) item
            self.dic.popitem(False)

# Time Complexity: O(1)
# Space Complexity: O(C)