class MyCircularDeque:

    def __init__(self, k):
        self.k = k
        self.q = [0] * k
        self.size = 0
        self.front = 0
        self.rear = -1

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k
        self.q[self.front] = value
        if self.size == 0:
            self.rear = self.front
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        if self.size == 0:
            self.front = self.rear
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k


d = MyCircularDeque(3)
print(d.insertLast(1))
print(d.insertLast(2))
print(d.insertFront(3))
print(d.insertFront(4))
print(d.getRear())
print(d.isFull())
print(d.deleteLast())
print(d.insertFront(4))
print(d.getFront())