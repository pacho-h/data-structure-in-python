from tabulate import tabulate

def addition(polynomial1, polynomial2):
    # get maximum degree
    polynomial1_maximum_degree = len(polynomial1)-1
    polynomial2_maximum_degree = len(polynomial2)-1
    maximum_degree = polynomial1_maximum_degree if polynomial1_maximum_degree >= polynomial2_maximum_degree else polynomial2_maximum_degree

    result = list()
    for index in range(maximum_degree+1, -1):
        degree = maximum_degree - index
        result.append(int(polynomial1[degree] if degree <= polynomial1_maximum_degree else 0) + int(polynomial2[degree] if degree <= polynomial2_maximum_degree else 0))

    return result.reverse()

print("""Array practice - Polynomial calculate
      Enter polynomial1
      ex) 2X^3 - 4X + 8 -> 2 0 -4 8
      """)

input_polynomial1 = input().split().reverse()

print("Enter polynomial2")
input_polynomial2 = input().split().reverse()

print(f"polynomial1:\n{tabulate([input_polynomial1],tablefmt='simple_outline')}")
print(f"polynomial2:\n{tabulate([input_polynomial2],tablefmt='simple_outline')}")

print("Addtion")
print(addition(input_polynomial1,input_polynomial2))

print("Multiplication")
