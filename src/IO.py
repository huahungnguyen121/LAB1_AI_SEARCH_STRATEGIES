# function return graph, start, des, searchStrategy, hValue
def readInput(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        return None, None, None, None, None

    graph = dict()
    hValue = dict()
    n = int(f.readline())
    str = f.readline().split()
    start = int(str[0])
    des = int(str[1])
    searchStrategy = int(str[2])
    for i in range(n):
        graph[i] = [int(par) for par in f.readline().split()]
    str = f.readline().split()
    for i in range(n):
        hValue[i] = int(str[i])
    f.close()
    return graph, start, des, searchStrategy, hValue

def writeOuput(expanded, path):
    try:
        f = open("../files/output.txt", "a")
    except FileNotFoundError:
        print("Error write file")
        return None
    if path is None:
        listToStr1 = ' '.join(map(str, expanded))
        f.write(listToStr1)
        f.write("\n")
        f.write("No path.")
        f.write("\n\n")
        f.close()
        return
    listToStr1 = ' '.join(map(str, expanded))
    listToStr2 = ' '.join(map(str, path))
    f.write(listToStr1)
    f.write("\n")
    f.write(listToStr2)
    f.write("\n\n")
    f.close()