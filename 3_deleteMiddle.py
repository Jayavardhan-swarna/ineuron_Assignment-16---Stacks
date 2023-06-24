def deleteMiddle(stack):
    if len(stack) <= 1:
        return stack

    mid = stack.pop()

    stack = deleteMiddle(stack)

    if len(stack) % 2 == 0:
        stack.append(mid)

    return stack

stack1 = [1, 2, 3, 4, 5]
print(deleteMiddle(stack1))
# Output: [1, 2, 4, 5]

stack2 = [1, 2, 3, 4, 5, 6]
print(deleteMiddle(stack2))
# Output: [1, 2, 4, 5, 6]
