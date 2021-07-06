from collections import deque
import queue

def printFrontier(frontier): #this function is used for testing
    temp = []
    while frontier.queue:
        temp.append(frontier.get())
    for i in temp:
        print((i[0], i[1], i[2]))
    for item in temp:
        frontier.put(item)

def UCS(graph, start, des):
    inFrontier = dict()
    visited = dict() # for marking visited states
    for state in graph:
        visited[state] = False
        inFrontier[state] = False

    node = (0, start, None) # node = (path cost, state, state's predecessor for finding path)
    explored = []
    frontier = queue.PriorityQueue() # a priority queue
    frontier.put(node)
    inFrontier[node[1]] = True

    while frontier.queue:
        node = frontier.get()
        
        if node[1] == des:
            explored.append((node[1], node[2]))
            return [node[0] for node in explored], findPath(explored) # return explored set and path from start to des
        explored.append((node[1], node[2]))
        visited[node[1]] = True

        child_state_list = []
        nodeIndex = 0
        for child_state in graph[node[1]]:
            if child_state != 0:
                child_state_list.append((nodeIndex, child_state)) # (node, path cost)
            nodeIndex += 1
        for child_state in child_state_list:
            if not visited[child_state[0]]:
                if inFrontier[child_state[0]]:
                    tup = (child_state[1] + node[0], child_state[0], node[1])
                    temp = []
                    while frontier.queue:
                        temp.append(frontier.get())
                    for item in temp:
                        if item[1] == child_state[0]:
                            if item[0] > child_state[1] + node[0]:
                                item = tup
                        frontier.put(item)
                else:
                    frontier.put((child_state[1] + node[0], child_state[0], node[1]))
                    inFrontier[child_state[0]] = True

    return [node[0] for node in explored], None # No path found

def findPath(explored):
    predecessorList = dict() # for searching predecessor of a node in explored set when finding path
    for node in explored:
        predecessorList[node[0]] = node[1]

    state, predecessor = explored[-1][0], explored[-1][1] # last node before des
    path = deque([state])
    while predecessor is not None:
        state = predecessor
        predecessor = predecessorList[state]
        path.appendleft(state)
    return list(path)