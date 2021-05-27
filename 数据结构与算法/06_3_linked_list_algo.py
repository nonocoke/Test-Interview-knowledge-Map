
"""
    1 Merge two sorted lists
    2 Find middle node
    3 Remove nth node from the end
    4 Detect cycle in a list
    5 Reverse singly-linked list
"""
from typing import Optional


class Node:
    def __init__(self, data: int, next=None):
        self.val = data
        self.next = next


# 有序链表合并  Merge two sorted linked list
def mergeSortedList(l1: Node, l2: Node) -> Optional[Node]:
    # if l1 is None and l2 is None: return None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    fake_head = Node(None)
    cur = fake_head
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return fake_head.next


# 单链表的中间结点
def findMiddleNode(head: Node) -> Optional[Node]:
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


# 删除倒数第n个节点。假设n大于0  Remove nth node from the end
def removeNthFromEnd(head: Node, n: int) -> Optional[Node]:
    """    n=2
    1->2->3->4->5
          |
    1->2->3---->5
    """
    # 先看链表有没有n个节点
    fast = head
    count = 0
    while fast and count < n:
        fast = fast.next
        count += 1
    # 没有n个节点
    if not fast and count < n:
        return head
    # 刚好n个节点，删除倒数第n个节点，就是删除头节点
    if not fast and count == n:
        return head.next

    # 同时遍历slow，fast，找到倒数第n个节点
    slow = head
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return head


# 检测环  Detect cycle in a list
def hasCycle(head: Node) -> bool:
    """
    1->2->3->4->5
          |     |
           _____
    """
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False


# 单链表反转  Reverse singly-linked list
def reverseList(head: Node) -> Optional[Node]:
    cur, reversed_head = head, None
    while cur:
        tmp = cur.next           # 暂存后继节点 cur.next
        cur.next = reversed_head # 修改 next 引用指向
        reversed_head = cur      # reversed_head 暂存 cur
        cur = tmp                # cur 访问下一节点
    return reversed_head

# 单链表反转 - 递归
def reverseListRecur(head: Node) -> Optional[Node]:
    def recur(cur, pre):
        if not cur:  # 递归到尾节点(cur = None), 退出
            return pre
        res = recur(cur.next, cur)  # 递归后续节点
        cur.next = pre              # 修改节点引用方向
        return res                  # 返回反转链表头节点
    
    return recur(head, None)

if __name__ == "__main__":
    pass
