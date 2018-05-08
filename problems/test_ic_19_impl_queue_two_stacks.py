from ic_19_impl_queue_two_stacks import Queue


def test_queue_two_stacks():
	qu = Queue()
	qu.enqueue('a')
	qu.enqueue('b')
	qu.enqueue('c')

	assert qu.dequeue() == 'a'
	assert qu.dequeue() == 'b'
	assert qu.dequeue() == 'c'
	assert qu.dequeue() is None


def test_queue_two_stacks_back_and_forth():
	qu = Queue()
	qu.enqueue('a')
	assert qu.dequeue() == 'a'
	qu.enqueue('b')
	qu.enqueue('c')
	assert qu.dequeue() == 'b'
	qu.enqueue('d')
	assert qu.dequeue() == 'c'
	assert qu.dequeue() == 'd'
	assert qu.dequeue() is None
