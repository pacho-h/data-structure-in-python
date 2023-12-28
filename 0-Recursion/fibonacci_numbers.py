def fibonacci_numbers(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_numbers(n - 2) + fibonacci_numbers(n - 1)


print("Recursion practice - fibonacci_numbers\nEnter a number")
input_number = int(input())

numbers_string = ""
for i in range(input_number + 1):
    numbers_string += f"{fibonacci_numbers(i)} "

print(f"Fibonacci_numbers({input_number}) = {numbers_string}")

"""
$ poetry run python fibonacci_numbers.py
Recursion practice - fibonacci_numbers
Enter a number
8
Fibonacci_numbers(8) = 0 1 1 2 3 5 8 13 21 
"""
