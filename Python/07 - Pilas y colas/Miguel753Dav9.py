# Pila/Stack (LIFO)

stack = []
stack.append(1) # push
stack.append(2) # push
stack.append(3) # push
print(stack)
# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack.pop())
print(stack_item)
print(stack)

# Cola/Queue (FIFO)
queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item = queue[0]

del queue[0]

print(queue_item)

print(queue.pop(0))

print(queue)