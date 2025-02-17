from utils import Stack


def convert_dec_to_binary(decNumber):
    rem_stack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        rem_stack.push(rem)
        decNumber = decNumber // 2 #quotient

    binString = ""
    while not rem_stack.is_empty():
        binString = binString + str(rem_stack.pop())

    return binString

print(convert_dec_to_binary(233))

def left_shift(stack):
    if stack:
        first_item = stack.pop(0)
        stack.append(first_item)
    return stack

def right_shift(stack):
    if stack:
        last_item = stack.pop()
        stack.insert(0, last_item)
    return stack

