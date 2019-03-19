from  Hackathon Project import recursion

def test_sum_array():

     assert recursion.sum_array([5,8,0,3,2])== 18, 'incorrect'
     assert recursion.sum_array([96,6,0,3,12])== 117, 'incorrect'

def test_fibonacci():
     assert recursion.fibonacci(6)==8, 'incorrect'
     assert recursion.fibonacci(10)==55, 'incorrect'


def test_factorial():
    assert recursion.factorial(12)==479001600, 'incorrect'
    assert recursion.factorial(8)==40320, 'incorrect'


def test_reverse():
    assert recursion.reverse("oarabile")=='elibarao', 'incorrect'
    assert recursion.reverse("plenty")=='ytnelp', 'incorrect'



from  Hackathon Project import sorting

def test_bubble_sort():
assert sorting.bubble_sort([3,9,6,8,12,8])==[3, 6, 8, 8, 9, 12], 'incorrect'
assert sorting.bubble_sort([1,9,6,3])==[1, 3, 6, 9], 'incorrect'



def test_merge_sort():
assert sorting.merge_sort([5, 2, 6, 8, 5, 8, 1])==[1, 2, 5, 5, 6, 8, 8], 'incorrect'
assert sorting.merge_sort([3, 12,46, 99, 5, 8, 1])==[1, 3, 5, 8, 12, 46, 99], 'incorrect'

def test_quicksort():
assert sorting.quicksort([4,20,3,15,2,27,16])==[2, 3, 4, 15, 16, 20, 27], 'incorrect'
assert sorting.uicksort([14,2,36,1,2,7,6])==[1, 2, 2, 6, 7, 14, 36], 'incorrect'
