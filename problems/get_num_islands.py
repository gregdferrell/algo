#
# Problem: Find the number of islands in a 2 dimensional array.
#
# Discover and return the total number of islands in the given 2 dimensional
# array. The two dimensional array has values of 0 (water) or -1 (land). An
# island can be made up of any number of elements of the arrays as long as
# those elements are directly above, below or beside one another, but not
# diagonal.


def find_number_of_islands(data):
    current_island = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            # Only examine if this is a new island: (val == -1)
            if data[x][y] == -1:
                # Increment island counter
                current_island += 1

                # Mark it
                data[x][y] = current_island

                # Recursively mark everything around it
                find_neighbor_islands(x, y, current_island, data)

    return current_island


def find_neighbor_islands(x, y, current_island, data):
    # Check previous array same position ("up")
    if x > 0 and len(data[x - 1]) > y and data[x - 1][y] == -1:
        data[x - 1][y] = current_island
        find_neighbor_islands(x - 1, y, current_island, data)

    # Check next array same position ("down")
    if x < len(data) - 1 and len(data[x + 1]) > y and data[x + 1][y] == -1:
        data[x + 1][y] = current_island
        find_neighbor_islands(x + 1, y, current_island, data)

    # Check same array next position ("right")
    if y < len(data[x]) - 1 and data[x][y + 1] == -1:
        data[x][y + 1] = current_island
        find_neighbor_islands(x, y + 1, current_island, data)

    # Check same array previous position ("left")
    if y > 0 and data[x][y - 1] == -1:
        data[x][y - 1] = current_island
        find_neighbor_islands(x, y - 1, current_island, data)

