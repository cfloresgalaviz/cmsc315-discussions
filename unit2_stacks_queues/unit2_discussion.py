from collections import deque


class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("front from an empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0


def demonstrate_stack():
    print("\n=== STACK DEMO (Browser Back-Button History) ===")

    history = Stack()
    history.push("home.html")
    history.push("products.html")
    history.push("product_detail.html")
    history.push("checkout.html")

    print("Pages visited in order: home.html -> products.html -> product_detail.html -> checkout.html")
    print(f"Top of stack (peek): {history.peek()}")

    print("\nLIFO in action: the LAST page visited is the FIRST one 'back' returns to.")
    print("Pressing 'back' repeatedly (pop) shows pages in reverse visit order:")
    while not history.is_empty():
        print(f"  - {history.pop()}")

    try:
        history.pop()
    except IndexError as error:
        print(f"\nPopping an empty stack raised an error: {error}")

    try:
        history.peek()
    except IndexError as error:
        print(f"Peeking an empty stack raised an error: {error}")

    single_page = Stack()
    single_page.push("landing.html")
    single_page.pop()
    print(f"\nSingle-item stack empty after one pop? {single_page.is_empty()}")


def demonstrate_queue():
    print("\n=== QUEUE DEMO (Customer Support Ticket Queue) ===")

    tickets = Queue()
    tickets.enqueue("Ticket #101")
    tickets.enqueue("Ticket #102")
    tickets.enqueue("Ticket #103")
    tickets.enqueue("Ticket #104")

    print("Tickets submitted in order: #101, #102, #103, #104")
    print(f"Next ticket to be served (front): {tickets.front()}")

    print("\nFIFO in action: the FIRST ticket submitted is the FIRST one served.")
    print("Serving tickets in the order they were submitted (dequeue):")
    while not tickets.is_empty():
        print(f"  - {tickets.dequeue()}")

    try:
        tickets.dequeue()
    except IndexError as error:
        print(f"\nDequeuing an empty queue raised an error: {error}")

    try:
        tickets.front()
    except IndexError as error:
        print(f"Checking the front of an empty queue raised an error: {error}")

    single_ticket = Queue()
    single_ticket.enqueue("Ticket #999")
    single_ticket.dequeue()
    print(f"\nSingle-item queue empty after one dequeue? {single_ticket.is_empty()}")


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    demonstrate_stack()
    demonstrate_queue()


if __name__ == "__main__":
    main()
