import heapq

def isvalid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if c > m > 0:
        return False
    if (3 - c > 3 - m) and (3 - m > 0):
        return False
    return True

def successor(state):
    m, c, b = state
    moves = []
    if b == 1:
        if isvalid((m, c - 2, 0)):
            moves.append((m, c - 2, 0))
        if isvalid((m - 2, c, 0)):
            moves.append((m - 2, c, 0))
        if isvalid((m - 1, c - 1, 0)):
            moves.append((m - 1, c - 1, 0))
        if isvalid((m, c - 1, 0)):
            moves.append((m, c - 1, 0))
        if isvalid((m - 1, c, 0)):
            moves.append((m - 1, c, 0))
    else:
        if isvalid((m, c + 2, 1)):
            moves.append((m, c + 2, 1))
        if isvalid((m + 2, c, 1)):
            moves.append((m + 2, c, 1))
        if isvalid((m + 1, c + 1, 1)):
            moves.append((m + 1, c + 1, 1))
        if isvalid((m, c + 1, 1)):
            moves.append((m, c + 1, 1))
        if isvalid((m + 1, c, 1)):
            moves.append((m + 1, c, 1))
    return moves

def heuristic(state):
    m, c, _ = state
    return (m + c - 2) / 2

def astar(start_state):
    heap = []
    heapq.heappush(heap, (heuristic(start_state), 0, [start_state]))
    visited = set()
    while heap:
        _, cost, path = heapq.heappop(heap)
        current_state = path[-1]
        if current_state in visited:
            continue
        if current_state == (0, 0, 0): 
            return path
        visited.add(current_state)
        for child in successor(current_state):
            if child not in visited:
                new_path = path + [child]
                new_cost = cost + 1
                heapq.heappush(heap, (new_cost + heuristic(child), new_cost, new_path))
    return None

start_state = (3, 3, 1)
solution = astar(start_state)
if solution:
    print(solution)
else:
    print("No solution found")
