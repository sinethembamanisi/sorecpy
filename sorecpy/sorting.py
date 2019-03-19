#function 5
def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(len(items)):
        for j in range(0,len(items)-i-1):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]

    bubble_sort = items[:]
    return bubble_sort

#function 6
def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
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

    '''Return array of items, sorted in ascending order'''
    items.sort()
    return items
