from array_stack import ArrayStack


def evaluate_rpn(expression):
    stack = ArrayStack()
    operators = '+-*/'

    for token in expression.split():
        if token not in operators:
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(int(a / b))  # int() for integer division in Python 3.x

    return stack.pop()


# 사용 예제
print(evaluate_rpn('3 4 + 2 * 7 /'))  # 2
print(evaluate_rpn('5 1 2 + 4 * + 3 -'))  # 14
