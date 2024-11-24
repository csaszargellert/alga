import os
#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def maxSubarray(arr):
    cur_sum = 0
    max_sum = arr[0]
    max_subsequence = max(arr)

    for n in arr:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
        if n > 0:
            max_subsequence += n

    if max_subsequence > 0:
        max_subsequence -= max(arr)

    return [max_sum, max_subsequence]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
