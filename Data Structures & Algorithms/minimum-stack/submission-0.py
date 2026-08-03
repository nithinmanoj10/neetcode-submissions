class MinStack:

    def __init__(self):
        self.stack = []
        self.min_track = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_track) == 0:
            self.min_track.append(val)
        else:
            self.min_track.append(min(self.min_track[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_track.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_track[-1]
