def empty(stack):
    return len(stack) == 0

def push(stack, data):
    if data not in stack:
        stack.append(data)
        print("After push:", stack)
    else:
        print(f"{data} is duplicated.")
        print('Stack is: ', stack)

def pop(stack):
    if empty(stack):
        print('Stack is empty.')
    else:
        stack.pop()
        print("After pop:", stack)

stack = []

push(stack, 3)
push(stack, 2)
push(stack, 5)
push(stack, 7)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)

