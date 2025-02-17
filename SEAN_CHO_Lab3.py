class TwoStack:
    def __init__(self, n):
        self.size = n
        self.stack = [None] * n
        self.left_top = -1
        self.right_top = n

    def push_left(self, item):
        if self.left_top + 1 < self.right_top:
            self.left_top += 1
            self.stack[self.left_top] = item
        else:
            print("Stack Overflow: Left stack is full")

    def push_right(self, item):
        if self.right_top - 1 > self.left_top:
            self.right_top -= 1
            self.stack[self.right_top] = item
        else:
            print("Stack Overflow: Right stack is full")

    def pop_left(self):
        if self.left_top >= 0:
            item = self.stack[self.left_top]
            self.left_top -= 1
            return item
        else:
            print("Stack Underflow: Left stack is empty")
            return None

    def pop_right(self):
        if self.right_top < self.size:
            item = self.stack[self.right_top]
            self.right_top += 1
            return item
        else:
            print("Stack Underflow: Right stack is empty")
            return None

    def len_left(self):
        return self.left_top + 1

    def len_right(self):
        return self.size - self.right_top

    def transfer_to_left(self, n):
        if n <= self.len_right():
            for _ in range(n):
                item = self.pop_right()
                self.push_left(item)
        else:
            print("Not enough items in the right stack to transfer items.")

    def transfer_to_right(self, n):
        if n <= self.len_left():
            for _ in range(n):
                item = self.pop_left()
                self.push_right(item)
        else:
            print("Not enough items in the left stack to transfer items.")

# Driver code
ts = TwoStack(8)

ts.push_left(1)
ts.push_left(2)
ts.push_left(3)
print("Left Stack:", ts.stack[:ts.len_left()])

ts.push_right(9)
ts.push_right(8)
ts.push_right(7)
print("Right Stack:", ts.stack[ts.right_top:])

print("Popped from Left Stack:", ts.pop_left())
print("Popped from Right Stack:", ts.pop_right())

ts.transfer_to_left(2)
print("Left Stack after transfer:", ts.stack[:ts.len_left()])
print("Right Stack after transfer:", ts.stack[ts.right_top:])

ts.transfer_to_right(2)
print("Left Stack after transfer:", ts.stack[:ts.len_left()])
print("Right Stack after transfer:", ts.stack[ts.right_top:])

ts.push_left(3)
ts.push_left(4)
ts.push_left(5) # Left stack overflow
print("Left Stack Length:", ts.len_left())
ts.push_right(6)
ts.push_right(5)
ts.push_right(4) # Right stack overflow
print("Right Stack Length:", ts.len_right())

ts.pop_left()
ts.pop_left()
ts.pop_left()
ts.pop_left()
ts.pop_left() # Left stack underflow
ts.pop_right()
ts.pop_right()
ts.pop_right()
ts.pop_right()
ts.pop_right() # Right stack underflow

print("Left Stack Length:", ts.len_left())
print("Right Stack Length:", ts.len_right())