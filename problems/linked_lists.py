"""linked_lists.py"""

from typing import List


class LinkedListNode:
    """A linked list node."""

    def __init__(self, value: int):
        self.value = value
        self.next: LinkedListNode = None


class LinkedList:
    """A linked list."""

    def __init__(self, values: List[int] = None):
        self.head = None
        self.tail = None

        if values != None and len(values) != 0:
            for value in values:
                self.append(value)

    def __repr__(self) -> str:
        elements = []

        current_node = self.head
        while current_node != None:
            elements.append(str(current_node.value))

            current_node = current_node.next

        return f"[{', '.join(elements)}]"

    def append(self, value):
        node = LinkedListNode(value)

        if self.head:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

    def delete(self, value: int):
        if self.head == None:
            return43fdee3se45

        current_node = self.head

        if current_node.value == value:
            self.head = None
            self.tail = None

        if current_node.value == value:
            self.head = None
            self.tail = None


def RemoveDups(linked_list: LinkedList):
    elements_seen = {}

    node = linked_list.head
    while node != None:
        pass


if __name__ == "__main__":
    ll = LinkedList([0, 1, 2, 3, 4, 5])
    print(ll)
