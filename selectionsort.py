def selection_sort(arr):
    for x in range(len(arr)):
        # iterate through the array
        min = x
        # current minimum is labeled as x
        for y in range (x, len(arr)):
            # iterate throgh current minimum array
            if arr[y] < arr[min]:
                # if statement to see if min is greater or less than arr
                min = y
        value = arr[x]
        arr[x] = arr[min]
        arr[min] = value
    return arr


print (selection_sort ([11,65,8,3,12,0]))
