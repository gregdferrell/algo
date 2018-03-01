from ic_25_linked_list_nth_last_node import nth_to_last_node
from problem_solve_util import LinkedListNode


def test_nth_to_last_node():
    a = LinkedListNode('a')
    b = LinkedListNode('b')
    c = LinkedListNode('c')
    d = LinkedListNode('d')
    e = LinkedListNode('e')
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    assert not nth_to_last_node(6, a)
    assert nth_to_last_node(5, a) == a
    assert nth_to_last_node(4, a) == b
    assert nth_to_last_node(3, a) == c
    assert nth_to_last_node(2, a) == d
    assert nth_to_last_node(1, a) == e


def test_nth_to_last_node_no_list():
    assert not nth_to_last_node(1, None)


def test_nth_to_last_node_len_1():
    a = LinkedListNode('a')

    assert not nth_to_last_node(2, a)
    assert nth_to_last_node(1, a) == a


def test_nth_to_last_node_len_2():
    a = LinkedListNode('a')
    b = LinkedListNode('b')
    a.next = b

    assert not nth_to_last_node(3, a)
    assert nth_to_last_node(2, a) == a
    assert nth_to_last_node(1, a) == b
