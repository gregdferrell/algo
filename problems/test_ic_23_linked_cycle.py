from ic_23_linked_cycle import contains_cycle, contains_cycle_set_impl
from problem_solve_util import LinkedListNode


def test_set_impl_no_cycle():
	a = LinkedListNode('a')
	b = LinkedListNode('b')
	c = LinkedListNode('c')
	d = LinkedListNode('d')
	e = LinkedListNode('e')
	a.next = b
	b.next = c
	c.next = d
	d.next = e

	assert not contains_cycle_set_impl(a)


def test_set_impl_has_cycle_first():
	a = LinkedListNode('a')
	b = LinkedListNode('b')
	c = LinkedListNode('c')
	d = LinkedListNode('d')
	a.next = b
	b.next = c
	c.next = d
	d.next = a

	assert contains_cycle_set_impl(a)


def test_set_impl_has_cycle_second():
	a = LinkedListNode('a')
	b = LinkedListNode('b')
	c = LinkedListNode('c')
	d = LinkedListNode('d')
	a.next = b
	b.next = c
	c.next = d
	d.next = b

	assert contains_cycle_set_impl(a)


def test_contains_cycle_no_cycle():
	a = LinkedListNode('a')
	b = LinkedListNode('b')
	c = LinkedListNode('c')
	d = LinkedListNode('d')
	e = LinkedListNode('e')
	a.next = b
	b.next = c
	c.next = d
	d.next = e

	assert not contains_cycle(a)


def test_contains_cycle_has_cycle_first():
	a = LinkedListNode('a')
	b = LinkedListNode('b')
	c = LinkedListNode('c')
	d = LinkedListNode('d')
	a.next = b
	b.next = c
	c.next = d
	d.next = a

	assert contains_cycle(a)


def test_contains_cycle_has_cycle_second():
	a = LinkedListNode('a')
	b = LinkedListNode('b')
	c = LinkedListNode('c')
	d = LinkedListNode('d')
	a.next = b
	b.next = c
	c.next = d
	d.next = b

	assert contains_cycle(a)
