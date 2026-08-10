class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.total_capacity = capacity
        self.curr_capacity = 0

        self.lru_list = LRUList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.lru_list.update(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru_list.update(key)
        else:
            if self.curr_capacity < self.total_capacity:
                self.cache[key] = value
                self.lru_list.add(key)
                self.curr_capacity += 1
            else:
                least_key = self.lru_list.get_least_key()
                del self.cache[least_key]
                self.cache[key] = value
                self.lru_list.update_least(key)



class LRUNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next  
        
class LRUList:
    def __init__(self):
        self.least = None
        self.latest = None

    def get_least_key(self):
        return self.least.key

    def add(self, key):
        """Adds a new key to the LRU List and makes it the latest"""
        latest_node = LRUNode(key)
        
        if self.least == None and self.latest == None:
            self.least = latest_node
            self.latest = latest_node
        else:
            self.latest.next = latest_node
            self.latest = self.latest.next


    def update(self, key):
        """Finds the key in the LRU List and makes it the latest"""
        # print(f"Update({key}): ", end="")
        # self.print_lru_list()

        if self.latest.key == key:
            return

        if self.least != self.latest:
            prev = None
            curr = self.least

            while curr and curr.key != key:
                prev = curr
                curr = curr.next

            if prev == None:
                temp = self.least.next
                self.least.next = None
                self.latest.next = self.least
                self.least = temp
                self.latest = self.latest.next
            else:
                prev.next = curr.next
                curr.next = None
                self.latest.next = curr
                self.latest = curr

    def update_least(self, key):
        """Update the least to the new key and make it the latest"""
        if self.least == self.latest:
            self.least.key = key
        else:
            self.least.key = key
            temp = self.least.next
            self.least.next = None
            self.latest.next = self.least
            self.least = temp
            self.latest = self.latest.next

    def print_lru_list(self):
        curr = self.least
        while curr:
            print(f"{curr.key}, ", end="")
            curr = curr.next
        print("")


