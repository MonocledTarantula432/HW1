class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.header = Node()
        self.trailer = Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0


def insert(self, k, value):
    if k < 0 or k > self.size:
        raise IndexError('Index is out of bounds')

    new_node = Node(value)
    current = self.header
    for i in range(k):  # Walk to k-1 th node
        current = current.next
    predecessor = current
    successor = current.next

    new_node.prev = predecessor
    predecessor.next = new_node

    successor.prev = new_node
    new_node.next = successor

    self.size += 1

    return new_node


def delete(self, k):
    if k < 0 or k >= self.size:
        raise IndexError('Index is out of bounds')

    current = self.header.next
    for i in range(k):  # Walk to k th node
        current = current.next
    predecessor = current.prev
    successor = current.next

    predecessor.next = successor
    successor.prev = predecessor

    self.size -= 1

    return current.value
