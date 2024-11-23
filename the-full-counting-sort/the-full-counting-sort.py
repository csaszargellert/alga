def createHelperArray(number_of_subarrays):
    array = []
    for _ in range(number_of_subarrays):
        array.append([])
    return array

def getMaxIndex(arr):
    index_array = []
    for i in range(len(arr)):
        index_array.append(int(arr[i][0]))
    return max(index_array)

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
def countSort(arr):
    half_length = len(arr) // 2
    helper_array = createHelperArray(getMaxIndex(arr) + 1)

    for i in range(len(arr)):
        index = int(arr[i][0])

        if i < half_length:
            helper_array[index].append('-')
        else:
            helper_array[index].append(arr[i][1])

    flatten_array = []
    for item in helper_array:
        flatten_array.extend(item)

    print(" ".join(flatten_array))
