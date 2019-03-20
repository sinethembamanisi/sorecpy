#function 5
def bubble_sort(items):

    #Return array of items, sorted in ascending order
    for i in range(len(items)):
        for j in range(0,len(items)-i-1):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]

    bubble = items[:]
    return bubble

#function 6
def merge_sort(items):


    '''Return array of items, sorted in ascending order'''
    length = len(items)

    if length > 1:
        mid = length // 2
        half1 = items[:mid]
        half2 = items[mid:]


#---------bubble_sorting for half1----------------
    x = len(half1)
    for a in range(x):
        for b in range(x-1):
            if (half1[a] < half1[b]):
                half1[a], half1[b] = half1[b], half1[a]


#----------bubble_sorting for half2--------------------

    y = len(half2)
    for a in range(y):
        for b in range(y-1):
            if (half2[a] < half2[b]):
                half2[a], half2[b] = half2[b], half2[a]


#----------------------------------------------------
    i = j = 0
    result = []
    while i < len(half1) and j < len(half2):
        if half1[i] < half2[j]:
            result.append(half1[i])
            i += 1
        else:
            result.append(half2[j])
            j += 1
    result += half1[i:]
    result += half2[j:]
    return result

#function 7
def quick_sort(items):

    #Return array of items, sorted in ascending order'''

    '''Return array of items, sorted in ascending order'''

    index=-1
    len_i = len(items)

    if len_i <= 1:
        # Logic Error
        # identified with test run [1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1]
        # len <= 1
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
