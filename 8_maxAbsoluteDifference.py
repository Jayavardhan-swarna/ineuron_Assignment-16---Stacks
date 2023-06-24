def maxAbsoluteDifference(arr):
    n = len(arr)
    leftSmaller = []
    rightSmaller = []

    # Calculate nearest left smaller elements
    for i in range(n):
        while leftSmaller and arr[leftSmaller[-1]] >= arr[i]:
            leftSmaller.pop()
        if leftSmaller:
            leftDiff = abs(arr[i] - arr[leftSmaller[-1]])
        else:
            leftDiff = 0
        leftSmaller.append(i)

    # Calculate nearest right smaller elements
    for i in range(n - 1, -1, -1):
        while rightSmaller and arr[rightSmaller[-1]] >= arr[i]:
            rightSmaller.pop()
        if rightSmaller:
            rightDiff = abs(arr[i] - arr[rightSmaller[-1]])
        else:
            rightDiff = 0
        rightSmaller.append(i)

    # Calculate maximum absolute difference
    maxDiff = 0
    for i in range(n):
        diff = abs(arr[leftSmaller[i]] - arr[rightSmaller[n - 1 - i]])
        maxDiff = max(maxDiff, diff)

    return maxDiff

# Example usage:
arr = [2, 1, 8]
result = maxAbsoluteDifference(arr)
print(result)  # Output: 1

arr = [2, 4, 8, 7, 7, 9, 3]
result = maxAbsoluteDifference(arr)
print(result)  # Output: 4

arr = [5, 1, 9, 2, 5, 1, 7]
result = maxAbsoluteDifference(arr)
print(result)  # Output: 1
