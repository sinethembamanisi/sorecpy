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

    #Return n!
    factor = 1
    for i in range(n):
        factor = n*i
    return factor

#function 4
def reverse(word):

    #Return word in reverse
    word_2 = ""
    for x in word:
        word_2= x + word_2

    return word_2

#function 5
