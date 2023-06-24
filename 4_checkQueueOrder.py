def checkQueueOrder(queue):
    stack = []
    secondQueue = []
    expected = 1

    while queue:
        if queue[0] == expected:
            queue.pop(0)
            expected += 1
        elif stack and stack[-1] == expected:
            secondQueue.append(stack.pop())
            expected += 1
        else:
            stack.append(queue.pop(0))

    while stack:
        if stack[-1] == expected:
            secondQueue.append(stack.pop())
            expected += 1
        else:
            break

    if not queue and not stack:
        return "Yes"
    else:
        return "No"

queue1 = [5, 1, 2, 3, 4]
print(checkQueueOrder(queue1))
# Output: Yes

queue2 = [5, 1, 2, 6, 3, 4]
print(checkQueueOrder(queue2))
# Output: No
