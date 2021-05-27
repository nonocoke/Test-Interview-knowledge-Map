
"""
    Queue based upon linked list
"""

from typing import Deque, Optional


class Node:
    def __init__(self, data: str, next=None):
        self.val = data
        self.next = next

class LinkdeQueue:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def enqueue(self, value: str):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self) -> Optional[Node]:
        if self.head:
            value = self.head.val
            self.head = self.head.next
            if not self.head:
                self.tail = Node
            return value

    def __repr__(self) -> str:
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next

        return "->".join(value for value in values)


if __name__ == "__main__":
    q = LinkdeQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(4):
        q.dequeue()
    print(q)

    q.enqueue("7")
    print(q)
