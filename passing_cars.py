def solution(A):
    # write your code in Python 3.6
    prefix_sum_array = []
    prefix_sum_array.append(A[0])
    n = len(A)
    for i in range(n - 1):
        new_value = prefix_sum_array[i] + A[i + 1] 
        prefix_sum_array.append(new_value)

    pairs_count = 0
    for i in range(n):
        if A[i] == 0 : 
            pairs_count += prefix_sum_array[n -1] - prefix_sum_array[i]
    return -1 if pairs_count > 1000000000 else pairs_count
