"""
Merge function for 2048 game
"""


def merge(line):
    """
    Accepts a line (row/column) and returns a
    merged copy of it for a 2048 grid
    """
    # get a copy of the line without spaces
    copy_of_line = close_gaps(line)
    index = 0
    while index < (len(line) - 1):
        curr_item = copy_of_line[index]
        next_item = copy_of_line[index + 1]
        # add current number with next if they are the same
        # and not 0
        if (curr_item == next_item) and (curr_item != 0):
            copy_of_line[index] = curr_item + next_item
            copy_of_line[index + 1] = 0
        # if the current item is 0, we might have merged
        # so we want to close gaps and work with new list
        if (curr_item == 0):
            copy_of_line = close_gaps(copy_of_line)
            curr_item = copy_of_line[index]
            # if current item is still 0, even after merge,
            # we are done
            if (curr_item == 0):
                return copy_of_line
            # index -1 so we can continue to merge non-merged
            # item
            else:
                index -= 1
        index += 1
    return copy_of_line


def close_gaps(line):
    """
    Closes the gaps in a row/column and returns new list
    without any gaps/spaces/0
    """
    insert_index = 0
    result = [0] * len(line)
    for index in range(len(line)):
        curr_value = line[index]
        if curr_value > 0:
            result[insert_index] = curr_value
            insert_index += 1
    return result
