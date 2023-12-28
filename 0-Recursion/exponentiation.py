def exponentiation(base, exponent):
    if exponent > 1:
        return base * exponentiation(base, exponent - 1)
    else:
        return base

print("Recursion practice - exponentiation\nEnter a base and a exponen\nbase:")
base = int(input())
print("exponent:")
exponent = int(input())

result = exponentiation(base, exponent)
print(f"{base}^{exponent} = {result}")

"""
$ poetry run python exponentiation.py
Recursion practice - exponentiation
Enter a base and a exponent
base:
2
exponent
8
2^8 = 256
"""
