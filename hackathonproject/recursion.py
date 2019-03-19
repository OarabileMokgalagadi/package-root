def sum_array(array):
    """calculate sum of all items in array"""
    if len(array) == 0:
        return 0
    else:
        return sum_array(array[1:]) + array[0]



def fibonacci(n):

     """Calculate nth term in fibonacci sequence"""

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):

    """ returns n! """

    if n <1:   # base case
        return 1
    else:
        return n * factorial( n - 1 )

def reverse(word):
     """ Return word in reverse"""

    wordlen = len(word)
    reversedword = ""
    for i in range(wordlen-1,-1,-1):
        reversedword += word[i]
    return reversedword
