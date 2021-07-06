from IO import readInput, writeOuput
from BFS import BFS
from DFS import DFS
from UCS import UCS
from IDS import IDS
from GBFS import GBFS
from AStar import AStar

inputFile1 = "../files/input_1.txt"
inputFile2 = "../files/input_2.txt"
inputFile3 = "../files/input_3.txt"

graph, start, des, searchStrategy, hValue = readInput(inputFile3) #replace inputFile1, inputFile2, inputFile3

if searchStrategy == 0:
    expanded, path = BFS(graph, start, des)
elif searchStrategy == 1:
    expanded, path = DFS(graph, start, des)
elif searchStrategy == 2:
    expanded, path = UCS(graph, start, des)
elif searchStrategy == 3:
    expanded, path = IDS(graph, start, des)
elif searchStrategy == 4:
    expanded, path = GBFS(graph, start, des, hValue)
elif searchStrategy == 5:
    expanded, path = AStar(graph, start, des, hValue)

print(expanded) #show the result
print(path)

writeOuput(expanded, path) #result will be appended in output.txt