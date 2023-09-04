 '''
    Binary Search
    -------------
    1.Array Should Be Sorted
    2.Specifing Lower & Upper Bounds.
    3.Getting a mid Value (lowerBound + higherBounnd // 2)
    4.if mid < elem make the existing mid element to new lower bound until it satisifes condition.
    5. if mid > elem make the mid element as new upper bound until the element is found.
'''
def binarySearch(arr,elem):

    lowerBound = 0
    higherBound = len(arr)-1
    
    while lowerBound <= higherBound:
        
        mid = lowerBound + higherBound // 2 

        if arr[mid] == elem:
            return mid
        
        elif arr[mid] > elem:
            higherBound = mid - 1

        elif arr[mid] < elem:
            lowerBound = mid + 1

    return -1
        
lstElem = [2,4,6,8,12,15]
elem_to_found = int(input('Enter Number To Find: '))
search_elem = binarySearch(lstElem,elem_to_found)

if search_elem == -1:
    print('Element Is Not Available !')
else:
    print('Element is Found At Position {}'.format(search_elem))
