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

    #Return array of items, sorted in ascending order'''
    if len(items)<2:
        return items

    result,mid=[],int(len(items)/2)
    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])

    while (len(y)>0) and (len(z)>0):
        if y[0]>z[0]:
            result.append(z.pop(0))
        else:
            result.append(y.pop(0))

    result.extend(y+z)
    return result

#function 7
def quick_sort(items):

    #Return array of items, sorted in ascending order'''
    def quick_sort(items):

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
