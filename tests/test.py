from sorecpy import sorting

def test_bubble_sort():
    """
    make sure bubble_sort works correctly
    """
    assert sorting.bubble_sort([8, 3, 2, 7, 4]) == [2, 3, 4, 7, 8], 'incorrect'
    #assert myFunction.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    #assert myFunction.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'
