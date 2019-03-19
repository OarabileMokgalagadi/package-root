def bubble_sort(items):
    """
    Return array of items, sorted in ascending order
    Args :
    items(array):list or array-like object containing numerical values

    returns:
    Return array of items, sorted in ascending order

    Examples:
    >>>bubble_sort([3,9,6,8,12,8])
       [3, 6, 8, 8, 9, 12]
    >>>bubble_sort([1,9,6,3])
       [1, 3, 6, 9]
    """
for i in range(len(items)):
        for j in range(i, len(items)):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
    return items


def merge_sort(items):

    """
     Return array of items, sorted in ascending order

     Args :
     items(array):list or array-like object containing numerical values

     returns:
     Return array of items, sorted in ascending order

     Examples:
     >>>merge_sort([5, 2, 6, 8, 5, 8, 1])
        [1, 2, 5, 5, 6, 8, 8]
    >>>merge_sort([3, 12,46, 99, 5, 8, 1])
       [1, 3, 5, 8, 12, 46, 99]
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



  def quicksort(items):

      """
      Return array of items, sorted in ascending order

      Args :
      items(array):list or array-like object containing numerical values

      returns:
      Return array of items, sorted in ascending order

      Examples:
      >>>quicksort([4,20,3,15,2,27,16])
      [2, 3, 4, 15, 16, 20, 27]
      >>>quicksort([14,2,36,1,2,7,6])
      [1, 2, 2, 6, 7, 14, 36]


      """

      if not items:
        return []

    pivots = [x for x in items if x == items[0]]
    lesser = quicksort([x for x in items if x < items[0]])
    greater = quicksort([x for x in items if x > items[0]])

    return lesser + pivots + greater
