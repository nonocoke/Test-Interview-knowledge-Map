
"""
  1 Push, pop on stack(based upon linked list)
  2 Assumes int for element type
"""

from os import name
from typing import Optional


class Node:
    def __init__(self, data: int, next=None):
        self.val = data
        self.next = next

class LinkedStack:
    """A stack based upon singly-linked list
    """
    def __init__(self):
        self.top: Node = None

    def push(self, value: int):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def pop(self) -> Optional[Node]:
        if self.top:
            value = self.top.val
            self.top = self.top.next
            return value

    def __repr__(self) -> str:
        cur = self.top
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next

        return " ".join(str(num) for num in nums)
        # return " ".join(f"{num}" for num in nums)

    
if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
