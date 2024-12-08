class TimeMap:

    def __init__(self):
        self.t_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t_map:
            self.t_map[key] = []
        self.t_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.t_map.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


timeMap = TimeMap()
# store the key "alice" and value "happy" along with timestamp = 1.
timeMap.set("alice", "happy", 1)
print(timeMap.get("alice", 1))           # return "happy"
# return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
print(timeMap.get("alice", 2))
# store the key "alice" and value "sad" along with timestamp = 3.
timeMap.set("alice", "sad", 3)
print(timeMap.get("alice", 3))           # return "sad"
