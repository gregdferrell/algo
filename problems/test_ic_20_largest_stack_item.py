from ic_20_largest_stack_item import MaxStackDouble, MaxStackIterate


def test_max_stack_iterate_middle():
	st = MaxStackIterate()
	st.push(1)
	st.push(3)
	st.push(5)
	st.push(4)
	st.push(10)
	st.push(4)
	st.push(9)

	assert st.get_max() == 10


def test_max_stack_iterate_first():
	st = MaxStackIterate()
	st.push(3)
	st.push(2)
	st.push(1)

	assert st.get_max() == 3


def test_max_stack_iterate_last():
	st = MaxStackIterate()
	st.push(1)
	st.push(2)
	st.push(3)

	assert st.get_max() == 3


def test_max_stack_double():
	st = MaxStackDouble()
	st.push(1)
	st.push(3)
	st.push(5)
	st.push(4)
	st.push(10)
	st.push(4)
	st.push(9)

	assert st.get_max() == 10


def test_max_stack_double_first():
	st = MaxStackDouble()
	st.push(3)
	st.push(2)
	st.push(1)

	assert st.get_max() == 3


def test_max_stack_double_last():
	st = MaxStackDouble()
	st.push(1)
	st.push(2)
	st.push(3)

	assert st.get_max() == 3
