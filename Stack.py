class stack():
    def __init__(self):
        self.top=-1
        self.size=1000
        self.st=[0]*self.size

    def push(self, x):
        self.top+=1
        self.st[self.top]=x

    def Top(self):
        x=self.st[self.top]
        return x

    def pop(self):
        x = self.st[self.top]  # Get the top element
        self.top -= 1
        return x

    def Size(self):
        return self.top+1


s=stack()
s.push(6)
s.push(3)
s.push(7)
print("Top of stack is before deleting any element", s.Top())
print("Size of stack before deleting any element", s.Size())
print("The element deleted is", s.pop())
print("Size of stack after deleting an element", s.Size())
print("Top of stack after deleting an element", s.Top())

