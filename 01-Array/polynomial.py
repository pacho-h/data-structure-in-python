from tabulate import tabulate


def get_maximum_degree(polynomial1, polynomial2):
    return (len(polynomial1) - 1, len(polynomial2) - 1)


def add(polynomial1, polynomial2):
    (
        polynomial1_maximum_degree,
        polynomial2_maximum_degree,
    ) = get_maximum_degree(polynomial1, polynomial2)

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
            (int(polynomial1[index]) if index <= polynomial1_maximum_degree else 0)
            + (int(polynomial2[index]) if index <= polynomial2_maximum_degree else 0),
        )

    return result


def multiply(polynomial1, polynomial2):
    polynomial1_maximum_degree, polynomial2_maximum_degree = get_maximum_degree(polynomial1, polynomial2)
    result_degree = polynomial1_maximum_degree + polynomial2_maximum_degree
    result = [0] * (result_degree + 1)

    for i in range(polynomial1_maximum_degree + 1):
        for j in range(polynomial2_maximum_degree + 1):
            result[i + j] += int(polynomial1[i]) * int(polynomial2[j])

    return result


print(
    """Array practice - Polynomial calculate
Enter polynomial1
ex) 2X^3 - 4X + 8 -> 2 0 -4 8""",
)

input_polynomial1 = input().split()

print('Enter polynomial2')
input_polynomial2 = input().split()

print(
    f"polynomial1:\n{tabulate([input_polynomial1], tablefmt='simple_outline')}",
)
print(
    f"polynomial2:\n{tabulate([input_polynomial2], tablefmt='simple_outline')}",
)

print('Addtion')
addition_result = add(input_polynomial1, input_polynomial2)
print(f"{tabulate([addition_result], tablefmt='simple_outline')}")

print('Multiplication')
multiplication_result = multiply(input_polynomial1, input_polynomial2)
print(f"{tabulate([multiplication_result], tablefmt='simple_outline')}")
