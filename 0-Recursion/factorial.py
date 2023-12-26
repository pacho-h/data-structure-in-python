def factorial(n, expression):
    if n <= 1:
        return (1, f"{expression}{n}")
    else:
        expression += f"{n} * "
        child, child_expression = factorial(n-1, expression)
        result = n * child
        return (result, child_expression)

print("Recursion practice - factorial\nEnter a number")
input_number = int(input())

(result, expression) = factorial(input_number, "")
print(f"{input_number}! = {expression}")
print(f" = {result}")

