def find_position(value, grid):
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if tile == value:
                return i, j

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 'X':
                goal_row, goal_col = find_position(state[i][j], goal_state)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def print_configuration(matrix):
    for row in matrix:
        print(row)
    print()

def generate_successors(state):
    successors = []
    blank_row, blank_col = next((i, j) for i, row in enumerate(state) for j, tile in enumerate(row) if tile == 'X')

    for i, j in [(blank_row - 1, blank_col), (blank_row, blank_col - 1), (blank_row, blank_col + 1), (blank_row + 1, blank_col)]:
        if 0 <= i < 3 and 0 <= j < 3:
            successor = [row.copy() for row in state]
            successor[blank_row][blank_col], successor[i][j] = successor[i][j], successor[blank_row][blank_col]
            successors.append(successor)

    return successors

def a_star(initial_state, goal_state):
    if initial_state == goal_state:
        return 0  # Already at the goal state

    open_list = [(manhattan_distance(initial_state, goal_state), 0, initial_state)]
    closed_set = set()

    while open_list:
        _, cost, current_state = min(open_list)

        if current_state == goal_state:
            return cost

        if tuple(map(tuple, current_state)) in closed_set:
            continue

        closed_set.add(tuple(map(tuple, current_state)))

        for successor in generate_successors(current_state):
            if tuple(map(tuple, successor)) not in closed_set:
                open_list.append((cost + 1 + manhattan_distance(successor, goal_state), cost + 1, successor))

    return -1  # If no solution is found

def take_input():
    configuration = []
    for i in range(3):
        row = input(f"Enter row {i + 1}: ").split()
        configuration.append(row)
    return configuration

print("Enter the initial configuration")
initial_configuration = take_input()
print("Enter the goal configuration")
goal_configuration = take_input()

result = a_star(initial_configuration, goal_configuration)

if result != -1:
    print(f"Solution found in {result} steps.")
else:
    print("No solution found.")
