from array_stack import ArrayStack


def find_path(maze, start, end):
    stack = ArrayStack()
    stack.push((start, [start]))

    rows, cols = len(maze), len(maze[0])
    visited = set()

    while not stack.is_empty():
        (current_position, path) = stack.pop()
        if current_position in visited:
            continue

        visited.add(current_position)
        row, col = current_position

        if current_position == end:
            return path

        # 상하좌우 이동
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if rows > r >= 0 == maze[r][c] and 0 <= c < cols:
                stack.push(((r, c), path + [(r, c)]))

    return None


# 사용 예제
problem = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
start_point = (0, 0)
end_point = (4, 4)
found_path = find_path(problem, start_point, end_point)
print(found_path)  # [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
