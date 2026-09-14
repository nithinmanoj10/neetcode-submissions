class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cpu_cycle = 0

        # (count_left, task)
        max_heap = []
        heapq.heapify(max_heap)

        # (count_left, task, next_avail_cycle)
        task_queue = collections.deque()

        # Initialize the max_heap
        for task, count in collections.Counter(tasks).items():
            heapq.heappush(max_heap, (-count, task))

        while len(max_heap) != 0 or len(task_queue) != 0:
            cpu_cycle += 1

            if len(task_queue) != 0 and task_queue[0][2] == cpu_cycle:
                count_left, task, _ = task_queue.popleft()
                heapq.heappush(max_heap, (-count_left, task))

            if len(max_heap) != 0:
                count_left, task = heapq.heappop(max_heap)
                
                if -count_left > 1:
                    task_queue.append((-count_left-1, task, cpu_cycle + n + 1))

        return cpu_cycle
                

        