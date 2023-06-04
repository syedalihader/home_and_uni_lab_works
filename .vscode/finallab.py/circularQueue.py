class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full.")
        elif self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return item

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            items = []
            temp = self.front
            while temp != self.rear:
                items.append(self.queue[temp])
                temp = (temp + 1) % self.capacity
            items.append(self.queue[self.rear])
            print("Queue:", items)
 
 
# Create a circular queue
my_circular_queue = CircularQueue(5)
my_circular_queue.enqueue(1)
my_circular_queue.enqueue(2)
my_circular_queue.enqueue(3)
my_circular_queue.display()
my_circular_queue.dequeue()
my_circular_queue.display()
