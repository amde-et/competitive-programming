class MyQueue:

    def __init__(self):
        self.A, self.B = [], []
        

    def push(self, x: int) -> None:
        self.A.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.B.pop()
        

    def peek(self) -> int:
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B[-1]

        

    def empty(self) -> bool:
        return not self.A and not self.B
