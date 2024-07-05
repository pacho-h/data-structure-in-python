from array_stack import ArrayStack


def is_balanced(expression):
    stack = ArrayStack()
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in matching_brackets.values():
            stack.push(char)
        elif char in matching_brackets.keys():
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return False
    return stack.is_empty()


# 사용 예제
print(is_balanced('(){}[]'))  # True
print(is_balanced('({[)]}'))  # False
print(is_balanced('({[]})'))  # True
