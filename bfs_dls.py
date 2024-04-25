graph =  {
    'a': ['b', 'c'] ,
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'e': 'h'
}
def dls(node, depth):
        visited = set()
        if depth < 0:
            return
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                dls(neighbor, depth - 1)


def breadth_first_search(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        current = queue.pop(0)
        print(current, end=' ')
        
      
        for neighbor in graph.get(current,[]):
             if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    print()



print("Depth-Limited Search (starting from vertex a, depth limit = 2):")
dls('a',1)
    

print("\nBreadth-First Search (starting from vertex 2):")
breadth_first_search(graph, 'a')

