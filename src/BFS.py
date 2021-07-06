from collections import deque

def BFS(graph, start, des):
    visited = dict() # for marking visited states
    for state in graph:
        visited[state] = False

    node = (start, None) # node = (state, state's predecessor for finding path)
    explored = []
    frontier = deque([node]) # perform like a queue
    visited[node[0]] = True

    if node[0] == des:
        return [node[0] for node in explored], findPath(explored, des) # return explored set and path from start to des

    while frontier:
        node = frontier.popleft() # pick the shallowest node in frontier
        explored.append(node)
        child_state_list = []
        nodeIndex = 0
        for child_state in graph[node[0]]:
            if child_state != 0:
                child_state_list.append(nodeIndex)
            nodeIndex += 1
        for child_state in child_state_list:
            if not visited[child_state]:
                if child_state == des:
                    return [node[0] for node in explored], findPath(explored, des) # return explored set and path from start to des
                frontier.append((child_state, node[0]))
                visited[child_state] = True

    return [node[0] for node in explored], None # No path found

def findPath(explored, des):
    predecessorList = dict() # for searching predecessor of a node in explored set when finding path
    for node in explored:
        predecessorList[node[0]] = node[1]

    state, predecessor = explored[-1][0], explored[-1][1] # last node before des
    path = deque([state])
    path.append(des)
    while predecessor is not None:
        state = predecessor
        predecessor = predecessorList[state]
        path.appendleft(state)
    return list(path)