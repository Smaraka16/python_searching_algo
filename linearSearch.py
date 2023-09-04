pos = -1
def linearSearch(arr,elem):
    for el  in range(len(arr)):
        if(arr[el] == elem):
            globals()['pos'] = el
            return True
    return False
    
lst_arr = [3,6,9,4,7]
elem_to_found = int(input('Enter Element  To Be Found: '))

if linearSearch(lst_arr,elem_to_found):
    print('Element Found at position {}'.format(pos))
else:
    print('Oops! Element Not Found ')
