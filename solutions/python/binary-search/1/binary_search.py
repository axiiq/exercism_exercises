def find(search_list, value, left=0, right=None):
    if right is None:
        right = len(search_list) - 1

    if left > right:
        raise ValueError("value not in array")

    mid_index = (left + right) // 2
    mid_value = search_list[mid_index]

    if mid_value == value:
        return mid_index
    
    elif mid_value > value:
        return find(search_list, value, left, mid_index - 1)

    else:
        return find(search_list, value, mid_index + 1, right)