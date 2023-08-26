"""
Just to test stuff.
"""

class MinStack:

    def __init__(self,val=None):
        if val:
            self.stack = [val]
        else:
            self.stack = []

    def push(self, val: int) -> None:
            if not self.stack or val<=self.stack[-1]:
                self.stack.append(val)
            else:
                tmp = self.stack.pop()
                self.stack.append(val)
                self.stack.append(tmp)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack.pop()


s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.stack)
print(s.getMin())
