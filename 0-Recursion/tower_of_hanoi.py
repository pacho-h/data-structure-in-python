def move_a_disk(departure, destination):
    print(f"{departure}의 가장 위에 있는 원판을 {destination}로 이동")


def move_disks(number_of_disks_to_move, departure, destination, stopover):
    if number_of_disks_to_move == 1:
        move_a_disk(departure, destination)
    else:
        move_disks(
            number_of_disks_to_move - 1, departure, stopover, destination
        )
        move_a_disk(departure, destination)
        move_disks(
            number_of_disks_to_move - 1, stopover, destination, departure
        )


print("Recursion practice - tower_of_hanoi\nEnter a natural number(1~5)")
input_number = int(input())
if input_number < 1 or input_number > 5:
    print("Input value is invalid")
else:
    move_disks(input_number, "A", "B", "C")

"""
$ poetry run python tower_of_hanoi.py
Recursion practice - tower_of_hanoi
Enter a natural number(1~5)
3
A의 가장 위에 있는 원판을 B로 이동
A의 가장 위에 있는 원판을 C로 이동
B의 가장 위에 있는 원판을 C로 이동
A의 가장 위에 있는 원판을 B로 이동
C의 가장 위에 있는 원판을 A로 이동
C의 가장 위에 있는 원판을 B로 이동
A의 가장 위에 있는 원판을 B로 이동

9
Input value is invalid
"""
