def restoreArray(adjacentPairs):
    from collections import defaultdict, deque

    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v in adjacentPairs:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Find the start node (node with only one neighbor)
    start = None
    for key in graph:
        if len(graph[key]) == 1:
            start = key
            break

    # Step 3: Reconstruct the array using BFS
    result = []
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Example usage:
adjacentPairs = [[2,1],[3,4],[3,2]]
print(restoreArray(adjacentPairs))  # Output: [1, 2, 3, 4] or [4, 3, 2, 1]
