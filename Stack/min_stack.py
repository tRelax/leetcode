class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        minim = self.stack[-1]

        while len(self.stack):
            minim = min(minim, self.stack[-1])
            tmp.append(self.stack.pop())
        while len(tmp):
            self.stack.append(tmp.pop())

        return minim


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print("AFTER PUSHING 1,2,0", minStack.stack)
print("GETTING MIN", minStack.getMin())
print("AFTER GET MIN", minStack.stack)
minStack.pop()
print("AFTER POP", minStack.stack)
print("TOP", minStack.top())
print("GET MIN AGAIN", minStack.getMin())
