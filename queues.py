def empty(queue):
    return len(queue) == 0

def enqueue(queue, data):
    queue.append(data)
    print("After enqueue: ", queue)

def dequeue(queue):
    if empty(queue):
        print('Queue is empty')
    else:
        queue.pop(0)
        print("After dequeue: ", queue)

queue = []

enqueue(queue, 2)
enqueue(queue, 4)
enqueue(queue, 1)
enqueue(queue, 8)
enqueue(queue, 5)

dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
