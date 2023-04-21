import numpy as numpy



training_file = "C:/Users/wyatt/Desktop/Computer Science/Assignment6/Training.txt"
training_data = numpy.loadtxt(training_file, dtype=int, delimiter=',')

#WikiVote_file = "C:/Users/wyatt/Desktop/Assignment6/WikiVote.txt"
#WikiVote_data = numpy.loadtxt(WikiVote_file, dtype=int, delimiter='    ')

def pageRank(data, a):
    realn = numpy.unique(data).shape[0]
    tempList = numpy.unique(data)
    listOfValues = [0] *tempList.shape[0]
    for i in range(tempList.shape[0]):
        listOfValues[i] = tempList[i]
    dataSize = data.shape[0] #amount of edges in the file
    Adjacency_matrix = numpy.zeros((realn,realn))#creates a matrix size n by n
    Adjacency_T_matrix = numpy.zeros((realn,realn))
    Nr = numpy.zeros((realn,realn))
    for i in range(realn):
        for j in range(realn):
            Nr[i][j] = 1/realn
    
    P_vector = [1] * realn
   
    #loops through every node in the file and puts them in an adjacency matrix
    for i in range(dataSize):
        tempX = data[i][0]
        tempY = data[i][1]
        x = listOfValues.index(tempX)
        y = listOfValues.index(tempY)
        Adjacency_matrix[x][y] = 1
        Adjacency_T_matrix[y][x] = 1
        
    count = 1
    otherPVector = [0]*realn
   
    normalized_matrix= numpy.zeros((realn,realn))
    temp = 0
    for i in range(realn):
        for j in range(realn):
            if(Adjacency_matrix[i][j] == 1):
                temp += 1
        for j in range(realn):
            if(Adjacency_matrix[i][j] == 1):
                normalized_matrix[i][j] = 1/temp
        temp = 0

    M = numpy.zeros((realn,realn))
    for i in range(realn):
        for j in range(realn):
            M[j][i] = (Nr[i][j]*a) + (normalized_matrix[i][j]*(1-a))
    while(count < 10):
        Pmax = max(P_vector)
        P_vector = numpy.matmul(M, P_vector)
        Pmax = max(P_vector)
        otherPVector = P_vector
        P_vector = P_vector * 1/Pmax
        count += 1
    
    count = 0
    hub = [1] * realn
    while(count < 10):
        hub = numpy.matmul(Adjacency_matrix, hub)
        Pmax = max(hub)
        otherHub = hub
        hub = hub * 1/Pmax
        count += 1
    normalized = numpy.linalg.norm(otherPVector)
    otherPVector = otherPVector/normalized
    for i in range(realn):
        print(listOfValues[i], " pageRank: ", otherPVector[i])
        print("Hub: ", hub[i])




pageRank(training_data, 0)
print("\n")
pageRank(training_data, .2)
print("\n")
pageRank(training_data, .4)
print("\n")
pageRank(training_data, .6)
print("\n")
pageRank(training_data, .8)
print("\n")
pageRank(training_data, 1)