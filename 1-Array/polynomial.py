from tabulate import tabulate


def addition(polynomial1, polynomial2):
    # get maximum degree
    polynomial1_maximum_degree = len(polynomial1) - 1
    polynomial2_maximum_degree = len(polynomial2) - 1
    maximum_degree = (
        polynomial1_maximum_degree
        if polynomial1_maximum_degree >= polynomial2_maximum_degree
        else polynomial2_maximum_degree
    )
    polynomial1.reverse()
    polynomial2.reverse()

    result = []
    for index in reversed(range(maximum_degree + 1)):
        result.append(
            (
                int(polynomial1[index])
                if index <= polynomial1_maximum_degree
                else 0
            )
            + (
                int(polynomial2[index])
                if index <= polynomial2_maximum_degree
                else 0
            ),
        )

    return result


print(
    """
Array practice - Polynomial calculate
Enter polynomial1
ex) 2X^3 - 4X + 8 -> 2 0 -4 8
""",
)

input_polynomial1 = input().split()

print("Enter polynomial2")
input_polynomial2 = input().split()

print(
    f"polynomial1:\n{tabulate([input_polynomial1],tablefmt='simple_outline')}",
)
print(
    f"polynomial2:\n{tabulate([input_polynomial2],tablefmt='simple_outline')}",
)

print("Addtion")
addition_result = addition(input_polynomial1, input_polynomial2)
print(f"{tabulate([addition_result],tablefmt='simple_outline')}")

# print("Multiplication")
