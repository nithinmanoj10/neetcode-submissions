class MedianFinder:

    def __init__(self):
        self.left_of_median = []
        self.right_of_median = []

        heapq.heapify(self.left_of_median)  # Max-Heap
        heapq.heapify(self.right_of_median) # Min-Heap

        self.curr_median = None
        self.curr_len = 0

    def addNum(self, num: int) -> None:
        self.curr_len += 1

        # adding the first number
        if self.curr_len == 1:
            heapq.heappush(self.left_of_median, -num)
            self.curr_median = num
            return

        if num <= self.curr_median:
            heapq.heappush(self.left_of_median, -num)
        else:
            heapq.heappush(self.right_of_median, num)

        # balance both sides if required
        # left side heavy
        if len(self.left_of_median) > len(self.right_of_median) + 1:
            max_num = -heapq.heappop(self.left_of_median)
            heapq.heappush(self.right_of_median, max_num)
        elif len(self.right_of_median) > len(self.left_of_median) + 1:
            min_num = heapq.heappop(self.right_of_median)
            heapq.heappush(self.left_of_median, -min_num)

        # compute the new median
        max_num = -self.left_of_median[0]
        min_num = self.right_of_median[0]
        if len(self.left_of_median) == len(self.right_of_median):
            self.curr_median = (max_num + min_num) / 2
        elif len(self.left_of_median) > len(self.right_of_median):
            self.curr_median = max_num
        else:
            self.curr_median = min_num


    def findMedian(self) -> float:
        return self.curr_median

        