def sortStack(stack):
    tmpStack = []
    
    while stack:
        temp = stack.pop()

        while tmpStack and tmpStack[-1] > temp:
            stack.append(tmpStack.pop())

        tmpStack.append(temp)
    
    while tmpStack:
        stack.append(tmpStack.pop())
    
    return stack

stack1 = [34, 3, 31, 98, 92, 23]
print(sortStack(stack1))
# Output: [3, 23, 31, 34, 92, 98]

stack2 = [3, 5, 1, 4, 2, 8]
print(sortStack(stack2))
# Output: [1, 2, 3, 4, 5, 8]
