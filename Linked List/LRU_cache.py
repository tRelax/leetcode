# using dictionary get O(1), put O(1) except finding min which is O(n)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.frequency = {}
        self.counter = 0

    def get(self, key: int) -> int:
        if key in self.frequency:
            self.counter += 1
            self.frequency[key] = self.counter
            return self.data[key]
        return -1

    def put(self, key: int, value: int) -> None:
        print("BEFORE", self.data, self.frequency)
        if len(self.data) >= self.capacity and key not in self.data:
            least_used_key = min(self.frequency, key=self.frequency.get)
            del self.data[least_used_key]
            del self.frequency[least_used_key]
        self.counter += 1
        self.data[key] = value
        self.frequency[key] = self.counter
        print("AFTER", self.data, self.frequency)

# using HashMap and LinkedList for get and put O(1) complexity


class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


lRUCache = LRUCache(2)
lRUCache.put(1, 10)  # cache: {1=10}
print(lRUCache.get(1))      # return 10
lRUCache.put(2, 20)  # cache: {1=10, 2=20}
lRUCache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
print(lRUCache.get(2))      # returns 20
print(lRUCache.get(1))  # -1

print("\n NEW \n")
lRUCache = LRUCache(2)  # null
lRUCache.put(1, 1)  # null
lRUCache.put(2, 2)  # null
print(lRUCache.get(1))  # 1
lRUCache.put(3, 3)  # null
print(lRUCache.get(2))  # -1
lRUCache.put(4, 4)  # null
print(lRUCache.get(1))  # -1
print(lRUCache.get(3))  # 3
print(lRUCache.get(4))  # 4
