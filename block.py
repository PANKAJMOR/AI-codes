import random

def print_state(state):
    print('\n'.join(state))

def heuristic(state, goal_state):
    count = 0
    for s, g in zip(state, goal_state):
        if s != g:
            count += 1
    return count


def hill_climbing(initial_state, goal_state):
    current_state = initial_state
    print("Initial State:")
    print_state(current_state)
    print("Goal State:", goal_state)
    print("Heuristic Value:", heuristic(current_state, goal_state))

    while True:
        neighbors = generate_neighbors(current_state)
        neighbors.append(current_state)

        # Sort all neighbors based on heuristic value
        neighbors.sort(key=lambda x: heuristic(x, goal_state))

        # If the best neighbor is worse than the current state, break
        if heuristic(neighbors[0], goal_state) >= heuristic(current_state, goal_state):
            break

        current_state = neighbors[0]
        print("Intermediate State:")
        print_state(current_state)
        print("Heuristic Value:", heuristic(current_state, goal_state))

    print("Reached Goal State:")
    print_state(current_state)

def generate_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and i < j:
                neighbor = list(state)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(''.join(neighbor))
    return neighbors

if __name__ == "__main__":
    initial_state = "BCDA"
    goal_state = "ABCD"

    hill_climbing(initial_state, goal_state)
