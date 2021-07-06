from collections import deque

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

def checkNewState(explored, curState, state):
    path = findPath(explored, curState)
    for node in path:
        if state == node:
            return False
    return True

def DFS(graph, start, des):
    node = (start, None) # node = (state, state's predecessor for finding path)
    explored = deque()
    frontier = deque([node]) # perform like a stack

    if node[0] == des:
        return [node[0] for node in explored], findPath(explored, des) # return explored set and path from start to des

    while frontier:
        node = frontier.pop() # pick the next node in the frontier
        if node[0] == des:
            return [node[0] for node in explored], findPath(explored, des) # return explored set and path from start to des
        explored.append(node)

        child_state_list = deque()
        nodeIndex = 0
        for child_state in graph[node[0]]:
            if child_state != 0:
                child_state_list.appendleft(nodeIndex)
            nodeIndex += 1
        for child_state in child_state_list:
            if checkNewState(explored, node[0], child_state):
                frontier.append((child_state, node[0]))

    return [node[0] for node in explored], None # No path found