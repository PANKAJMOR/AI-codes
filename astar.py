graph = {
    's': {'a': 1, 'g': 12},
    'a': {'s': 1, 'b': 2, 'c': 1},
    'b': {'a': 2, 'd': 1},
    'c': {'a': 1, 'd': 3, 'g': 4},
    'd': {'b': 1, 'c': 3, 'g': 2},
    'g': {'s': 12, 'c': 4, 'd': 2}
}

heuristics = {'s': 5, 'a': 3, 'b': 4, 'c': 2, 'd': 6, 'g': 0}

start = 's'
goal = 'g'

def astar(start, goal):
    closeset = set()
    openset = set()
    openset.add(start)

    camefrom = {}

    g_score = {node: float('inf') for node in graph}   # actual 
    f_score = {node: float('inf') for node in graph}   #heuristic-
    g_score[start] = 0   
    f_score[start] = heuristics[start]
    print(g_score)

    while openset:
        current = min(openset, key=lambda node: f_score[node])

        if current == goal:
            return construct_path(camefrom, current), g_score[current]

        openset.remove(current)
        closeset.add(current)

        for neighbor in graph[current]:
            if neighbor in closeset:
                continue

            tentative_gscore = g_score[current] + graph[current][neighbor]
            if tentative_gscore >= g_score[neighbor]:
                continue

            camefrom[neighbor] = current
            g_score[neighbor] = tentative_gscore
            f_score[neighbor] = g_score[neighbor] + heuristics[neighbor]
            if neighbor not in openset:
                openset.add(neighbor)

    return -1, -1

def construct_path(camefrom, current):
    totalPath = []
    while current in camefrom:
        totalPath.append(current)
        current = camefrom[current]
    totalPath.append(current)
    return totalPath[::-1]

if __name__ == "__main__":
    path, cost = astar(start, goal)

    if path != -1:
        print("Path is:", end="")
        for node in path:
            print(str(node) + "-->", end="")
        print(goal)
        print("Cost =", cost)
    else:
        print("Goal not reachable")


