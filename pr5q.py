class MyCircularQueue:

    def __init__(self, k):
        self.k = k
        self.q = [0] * k
        self.size = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k


q = MyCircularQueue(3)
print(q.enQueue(1))
print(q.enQueue(2))
print(q.enQueue(3))
print(q.enQueue(4))
print(q.Rear())
print(q.isFull())
print(q.deQueue())
print(q.enQueue(4))
print(q.Rear())