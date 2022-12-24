class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x
        

    def top(self) -> int:
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
