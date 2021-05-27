
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

    def get_top_value(self) -> int:
        if self.top:
            return self.top.val

    def __repr__(self) -> str:
        cur = self.top
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next

        return " ".join(str(num) for num in nums)
        # return " ".join(f"{num}" for num in nums)


class NewLinkedStack(LinkedStack):

    def is_empty(self):
        return not self.top


class Broweser():
    
    def __init__(self):
        self.forward_stack = NewLinkedStack()  # 往右
        self.back_stack = NewLinkedStack()     # 往左

    def can_forward(self):
        return False if self.forward_stack.is_empty() else True

    def can_back(self):
        return False if self.back_stack.is_empty() else True

    def back(self):
        # print("back: <--", self.back_stack)
        if self.back_stack.is_empty():
            return
        _top = self.back_stack.pop()
        self.forward_stack.push(_top)
        # print("forward -->: ", self.forward_stack)
        print("back to & cur in %s" % self.back_stack.get_top_value(), end="\n")
    
    def forward(self):
        # print("forward -->: ", self.forward_stack)
        if self.forward_stack.is_empty():
            return
        _top = self.forward_stack.pop()
        self.back_stack.push(_top)
        # print("back: <--", self.back_stack)
        print("forward to  & cur in %s" % _top, end="\n")

    def open(self, url):
        print("Open new url %s" % url, end="\n")
        self.back_stack.push(url)


def test_linked_stack():
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
    

def test_browser():
    browser = Broweser()
    browser.open('www.a')
    browser.open('www.b')
    browser.open('www.c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()


if __name__ == "__main__":
    test_linked_stack()
    test_browser()
