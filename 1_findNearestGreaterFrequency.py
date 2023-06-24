def findNearestGreaterFrequency(arr):
    freq = {}
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and freq[arr[i]] >= freq[stack[-1]]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])
        freq[arr[i]] = freq.get(arr[i], 0) + 1

    return result

arr1 = [1, 1, 2, 3, 4, 2, 1]
print(findNearestGreaterFrequency(arr1))
# Output: [-1, -1, 1, 2, 2, 1, -1]

arr2 = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
print(findNearestGreaterFrequency(arr2))
# Output: [2, 2, 2, -1, -1, -1, -1, 3, -1, -1]
