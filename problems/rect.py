#
# Problem: Write a function to find the rectangular intersection of two given rectangles.
#

# Rectangles are dicts with the following props:
#
# my_rectangle = {
# 	# Coordinates of bottom-left corner
# 	'left_x': 1,
# 	'bottom_y': 1,
#
# 	# Width and height
# 	'width': 6,
# 	'height': 3,
# }


def find_x_overlap(rect1, rect2):
	"""
	Return left_x and width of overlapping x of two rects
	"""
	r1left = rect1['left_x']
	r1right = r1left + rect1['width']
	r2left = rect2['left_x']
	r2right = r2left + rect2['width']

	highest_start_point = r1left if r1left >= r2left else r2left
	lowest_end_point = r1right if r1right <= r2right else r2right

	if highest_start_point < lowest_end_point:
		return highest_start_point, lowest_end_point - highest_start_point
	else:
		return None


def find_y_overlap(rect1, rect2):
	"""
	Return bottom_y and height of overlapping y of two rects
	"""
	r1bottom = rect1['bottom_y']
	r1top = r1bottom + rect1['height']
	r2bottom = rect2['bottom_y']
	r2top = r2bottom + rect2['height']

	highest_start_point = r1bottom if r1bottom >= r2bottom else r2bottom
	lowest_end_point = r1top if r1top <= r2top else r2top

	if highest_start_point < lowest_end_point:
		return highest_start_point, lowest_end_point - highest_start_point
	else:
		return None


def solution(rect1, rect2):
	result = {
		'left_x': 0,
		'bottom_y': 0,
		'width': 0,
		'height': 0,
	}

	x_overlap = find_x_overlap(rect1, rect2)
	if x_overlap:
		result['left_x'] = x_overlap[0]
		result['width'] = x_overlap[1]
		y_overlap = find_y_overlap(rect1, rect2)
		if y_overlap:
			result['bottom_y'] = y_overlap[0]
			result['height'] = y_overlap[1]
			return result

	return None
