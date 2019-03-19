def bubble_sort(items):
    """Return array of items, sorted in ascending order"""
    for i in range(len(items)):
        for j in range(i, len(items)):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
    return items


def merge_sort(items):

    """
     Return array of items, sorted in ascending order

    """

    if len(items) < 2:
        return items

    mid = len(items) // 2

    left_items = merge_sort(items[:mid])
    right_items = merge_sort(items[mid:])

    return merge(left_items, right_items)

def merge(left, right):

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


def quick_sort(items):
    """Return array of items, sorted in ascending order"""
    if not items:
        return []
    pivots = [x for x in items if x == items[0]]
    lesser = quicksort([x for x in items if x < items[0]])
    greater = quicksort([x for x in items if x > items[0]])
    return lesser + pivots + greater
