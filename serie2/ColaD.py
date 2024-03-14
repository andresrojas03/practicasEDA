class CircularQ:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1 #head pointer
        self.rear = -1 #tail pointer
    
    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    
    def enqueue(self, item):
        if self.isFull():
            print("\nCicular Queue is Full!")
        else:
            if self.isEmpty():
                self.front = 0
            self.rear = (self.rear + 1 ) % self.capacity
            self.queue[self.rear] = item
            print("Inserted Item -> " + str(item))
        
    def dequeue(self):
        if self.isEmpty():
            print("\nQueue is Empty!!")
        elif self.front == self.rear:

            temp = self.queue[self.front]
            self.front = self.rear = -1
            print("Dequeued item -> " + str(temp))
            return temp 
        
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            print("Dequeued item -> " + str(temp))
            return temp
        
    
    def display(self):
        if self.isEmpty():
            print("La cola esta vacia.")
            return
        elif self.front <= self.rear:
            print("Elementos en la cola:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Elementos en la cola:")
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty."
        elif self.front <= self.rear:
            return "Items in Queue: " + ", ".join(str(self.queue[i]) for i in range(self.front, self.rear + 1))
        else:
            return "Items in Queue: " + ", ".join(str(self.queue[i]) for i in range(self.front, self.capacity)) + \
                   ", " + ", ".join(str(self.queue[i]) for i in range(0, self.rear + 1))
