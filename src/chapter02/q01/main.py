import unittest

from typing import Optional
from typing import List


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return '<Node: {}>'.format(self.data)


class LinkList:
    def __init__(self, head: Optional[Node] = None):
        self.head = head

    def __repr__(self) -> str:
        values = []
        cur_node = self.head
        while cur_node:
            values.append(str(cur_node))
            cur_node = cur_node.next
        return '<Link: {}>'.format(' '.join(values))

    def __eq__(self, other: 'LinkList') -> bool:
        equal = True
        left, right = self.head, other.head
        while left.next is not None or right.next is not None:
            if left.next is not None and right.next is not None:
                if left.data != right.data:
                    equal = False
                    break
                left, right = left.next, right.next
            else:
                equal = False
                break
        return equal

    def push(self, data: int):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    @classmethod
    def from_list(cls, source: List[int]) -> 'LinkList':
        new_list = cls()
        for i in source:
            new_list.push(i)
        return new_list


def delete_duplicates(link: LinkList) -> LinkList:
    unique_data = set()
    prev: Optional[Node] = None
    node: Optional[Node] = link.head
    while node:
        if (node.data in unique_data):
            prev.next = node.next
            node = node.next
        else:
            unique_data.add(node.data)
            prev, node = node, node.next
    return link


class TestCase(unittest.TestCase):
    def test_case1(self):
        source = LinkList.from_list([1, 2, 3, 2])
        target = LinkList.from_list([1, 3, 2])
        source = delete_duplicates(source)
        self.assertEqual(source, target)

    def test_case2(self):
        source = LinkList.from_list([1, 2, 3, 2, 3])
        target = LinkList.from_list([1, 2, 3])
        source = delete_duplicates(source)
        self.assertEqual(source, target)


class EqualTestCase(unittest.TestCase):

    def test_eq_not_empty(self):
        l = LinkList.from_list([1, 2, 3, 4])
        r = LinkList.from_list([1, 2, 3, 4])
        self.assertEqual(l, r)

    def test_not_eq(self):
        l = LinkList.from_list([1, 2, 3])
        r = LinkList.from_list([1])
        self.assertNotEqual(l, r)

if __name__ == "__main__":
    unittest.main()