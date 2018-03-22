from ic_24_reverse_linked_list import reverse_linked_list
from problem_solve_util import LinkedListNode


def test_reverse_linked_list():
	a = LinkedListNode(1)
	b = LinkedListNode(2)
	c = LinkedListNode(3)
	d = LinkedListNode(4)
	# put b after a
	a.next = b
	# put c after b
	b.next = c
	# put d after c
	c.next = d

	assert a.value == 1
	assert a.next.value == 2
	assert a.next.next.value == 3
	assert a.next.next.next.value == 4

	# Reverse list and get new head node
	new_head_node = reverse_linked_list(a)

	assert new_head_node.value == 4
	assert new_head_node.next.value == 3
	assert new_head_node.next.next.value == 2
	assert new_head_node.next.next.next.value == 1


def test_reverse_linked_list_size_1():
	a = LinkedListNode(1)

	assert a.value == 1
	assert a.next is None

	# Reverse list and get new head node
	new_head_node = reverse_linked_list(a)

	assert new_head_node.value == 1
	assert new_head_node.next is None
