#function 1
def sum_array(array):

    #Returns sum of all items in array
    total = 0
    for i in array:
        total +=  array[i-1]
    return total

#function 2
def fibonacci(n):

    #Return nth term in fibonacci sequence
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#function 3
def factorial(n):

    '''Return n!'''

    result = 1
    for i in range(1,n+1,1):
        result *= i
    return result

#function 4
def reverse(word):

    '''Return word in reverse'''

    rev_word =""

    for i in word:
        rev_word = i + rev_word
    return rev_word
