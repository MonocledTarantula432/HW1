from utils import Stack

def is_valid_symbol_string(symbols):
    stack = Stack()
    pairs = {"(": ")", "[": "]", "{": "}"}

    for symbol in symbols:
        if symbol in pairs:  # If opening symbol, push onto the stack
            stack.push(symbol)
        else:  # If closing symbol, check for balance
            if stack.is_empty() or pairs[stack.pop()] != symbol:
                return False

    return stack.is_empty()

print(is_valid_symbol_string('{({([][])}())}'))  # Yes
print(is_valid_symbol_string('[{()]'))  # No
