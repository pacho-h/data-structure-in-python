class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def append(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        polynomial_str = ''
        while current:
            if current.exponent == 0:
                polynomial_str += f'{current.coefficient}'
            else:
                polynomial_str += f'{current.coefficient}x^{current.exponent}'
            if current.next:
                polynomial_str += ' + '
            current = current.next
        print(polynomial_str)


# 3x^2 + 4x^1 + 2
poly = Polynomial()
poly.append(3, 2)
poly.append(4, 1)
poly.append(2, 0)
poly.display()
