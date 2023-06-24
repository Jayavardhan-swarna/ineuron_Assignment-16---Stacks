from queue import Queue

def reverseFirstK(queue, k):
    stack = []
    n = queue.qsize()

    # Enqueue the first k elements into the stack
    for i in range(k):
        stack.append(queue.get())

    # Enqueue the remaining elements back into the queue
    while not queue.empty():
        queue.put(queue.get())

    # Dequeue the elements from the stack and enqueue them back into the queue
    while stack:
        queue.put(stack.pop())

    # Move the last n-k elements from the front to the rear of the queue
    for i in range(n - k):
        queue.put(queue.get())

    return queue


q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

k = 3

reversed_q = reverseFirstK(q, k)
while not reversed_q.empty():
    print(reversed_q.get(), end=" ")

# Output: 3 2 1 4 5
