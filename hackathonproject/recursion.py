def sum_array(array):
    """calculate sum of all items in array.

    Args:
     array(items):list or array-like object containing numerical values
    Returns:
    int: sum of items in array

    Examples:
     >>>sum_array([5,8,0,3,2])
      18
      >>> sum_array([96,6,0,3,12])
      117
""""
    if len(array) == 0:
        return 0
    else:
        return sum_array(array[1:]) + array[0]



 def fibonacci(n):

     """"
     Calculate nth term in fibonacci sequence

     Args:
        n (int): nth term in fibonacci sequence to calculate

     Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

      Examples:
        >>> fibonacci(6)
        8
        >>>fibonacci(10)
        55
        """

        if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

    def factorial(n)

   """

   """

   Return n!
      Arg:
        n(int):the number that we want to calculate the factorial for

      Returns: return
      int: the factorial of n
      Examples:
          >>>factorial(12)
      479001600
          >>>factorial(8)
      40320
    """

    if n <1:   # base case
        return 1
    else:
        return n * factorial( n - 1 )


  def reverse(word):
     """ Return word in reverse
      Args:
          word(string):word to reverse in the function
      Returns:
         string:word in reverse
      Examples:
      >>>reverse("oarabile")
         'elibarao'
     >>>reverse("plenty")
         'ytnelp'
         """

    wordlen = len(word)
    reversedword = ""
    for i in range(wordlen-1,-1,-1):
        reversedword += word[i]
    return reversedword
