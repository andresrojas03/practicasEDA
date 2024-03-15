class deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def add_front(self, item):
        self.items.insert(0, item)
        print(f"Item enqueued in front -> {item}")
    
    def add_rear(self, item):
        self.items.append(item)
        print(f"Item enqueued in rear -> {item}")

    def remove_front(self):
        if not self.isEmpty():
            x = self.items.pop(0)
            print(f"Item dequeued from front -> {x} ")
            return x
            
        else:
            print("Queue is Empty!")
    
    def remove_rear(self):
        if not self.isEmpty():
            x = self.items.pop()
            print(f"Dequeued Item fron rear -> {x}")
            return x
        else:
            print("Queue is Empty!")

    def size(self):
        return len(self.items)
    
    def peekfront(self):
        if not self.isEmpty():
            peek = self.items[0]
            print(f"Here's the Item in peek front -> {peek}")
            return peek
        else:
            print("Queue is Empty!")
    
    def peekrear(self):
        if not self.isEmpty():
            peek = self.items[-1]
            print(f"Here's the Item in peek rear -> {peek} ")
            return peek
        else:
            print("Queue is Empty!")
    
    def __str__(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return f"Those are the elements in the Queue: {self.items}"
