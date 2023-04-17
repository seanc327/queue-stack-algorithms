class Queue:

    def __init__(self):  # constructor function
        self.items = []

    def isEmpty(self):  # returns True if the queue is empty or False otherwise
        return len(self.items) == 0

    def len(self):  # returns the number of items in the queue
        return len(self.items)

    def peek(self):  # returns the item at the front of the queue
        if self.isEmpty():
            return None
        return self.items[0]

    def add(self, item):  # adds item to the rear of the queue
        self.items.append(item)

    def pop(self):  # removes and returns the item at the front of the queue
        return self.items.pop(0)

    def remove(self, index):  # removes and returns the item at index of the queue
        if index >= len(self.items) or index < 0:
            return None
        return self.items.pop(index)

def stackToQueue(stack):

    queue = Queue()

    for item in reversed(stack):
        queue.add(item)
    return queue

if __name__ == "__main__":
    stack = [1,2,3]
    res = stackToQueue(stack)
    print(res) # expected (LinkedQueue): 3, 2, 1
