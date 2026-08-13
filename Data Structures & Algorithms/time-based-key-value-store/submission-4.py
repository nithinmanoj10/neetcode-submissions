class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}
            self.map[key]["timestamps"] = []
            self.map[key]["values"] = []
        
        self.map[key]["timestamps"].append(timestamp)
        self.map[key]["values"].append(value)
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        left = 0
        right = len(self.map[key]["timestamps"]) - 1
        curr_max_time = -1
        curr_max_idx = -1

        while left <= right:
            mid = left + int((right - left) / 2)

            if self.map[key]["timestamps"][mid] > curr_max_time and self.map[key]["timestamps"][mid] <= timestamp:
                curr_max_time = self.map[key]["timestamps"][mid]
                curr_max_idx = mid

            if self.map[key]["timestamps"][mid] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if curr_max_idx == -1:
            return ""

        return self.map[key]["values"][curr_max_idx]
