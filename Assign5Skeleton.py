import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy
import random
import time

#filename = "networkDatasets/toyN.txt"
toyFile = "toyN.txt"
toyData = numpy.loadtxt(toyFile,dtype=int,delimiter=' ')

hcNetworkFile = "C:/Users/wyatt/Desktop/Assignment5/HcNetwork.txt"
hcNetworkData = numpy.loadtxt(hcNetworkFile, dtype = int, delimiter= ' ')

hprdNetworkFile = "C:/Users/wyatt/Desktop/Assignment5/HprdNetwork.txt"
hprdNetworkData = numpy.loadtxt(hprdNetworkFile, dtype = int, delimiter= ' ')

karateFile = "C:/Users/wyatt/Desktop/Assignment5/karate.txt"
karateData = numpy.loadtxt(karateFile, dtype = int, delimiter= ' ')




def degree_distribution(data):
    dataSize = data.shape[0] #amount of edges in the file
    n = max(max(data[:,0]),max(data[:,1]))+1 #The biggest number that appears in a file
    sums = [0]*n    #A list that hold the degrees of every node in the file
    numbers= [0]*n  #Every node that appears in the file
    Adjacency_matrix = numpy.zeros((n,n)) #creates a matrix size n by n
    
    #loops through every node in the file and puts them in an adjacency matrix
    for i in range(dataSize):
        x = data[i][0]
        y = data[i][1]
        Adjacency_matrix[x-1][y-1] = 1
        Adjacency_matrix[y-1][x-1] = 1
        
    #A loop that puts every number 0 through n in the numbers list and sums each row of the adjacency matrix
    for i in range(n):
        numbers[i] = i + 1
        sums[i] = sum(Adjacency_matrix[i])
        plt.scatter(sums[i], numbers[i], cmap='rainbow', alpha=1, edgecolors='b')

def clustering_coefficient(data):
    dataSize = data.shape[0] #amount of edges in the file
    n = max(max(data[:,0]),max(data[:,1]))+1 #The biggest number that appears in a file
    sums = [0]*n    #A list that hold the degrees of every node in the file
    numbers= [0]*n  #Every node that appears in the file
    Vi_coefficients = [0]*n
    Adjacency_matrix = numpy.zeros((n,n)) #creates a matrix size n by n
    
    #loops through every node in the file and puts them in an adjacency matrix
    for i in range(dataSize):
        x = data[i][0]
        y = data[i][1]
        Adjacency_matrix[x-1][y-1] = 1
        Adjacency_matrix[y-1][x-1] = 1
        
    #A loop that puts every number 0 through n in the numbers list and sums each row of the adjacency matrix
    for i in range(n):
        numbers[i] = i + 1
        sums[i] = sum(Adjacency_matrix[i])
    
    #gets the coefficient of node Vi
    for i in range(n):
        if(sums[i] < 2):
            Vi_coefficients[i] = 0
        else:
            Vi_coefficients[i] = (2 * dataSize)/(sums[i] * (sums[i]-1))
    average = sum(Vi_coefficients)/n
    print (average)
    

print("toy data: ")   
degree_distribution(toyData)     
clustering_coefficient(toyData)
print("karate data: ")
degree_distribution(karateData)
clustering_coefficient(karateData)
print("hrpd Network data: ")
degree_distribution(hprdNetworkData)
clustering_coefficient(hprdNetworkData)
print("hc Network data")
degree_distribution(hcNetworkData)
clustering_coefficient(hcNetworkData)
#remember python index the entries from 0 to n-1.
#populate A..iterate over X and populate entries in A
#Since this is an undirected graph, when you read an edge, you have to update two entries
#toyN 1 2, #you should put A[0,1]=1 and A[1,0]=1
#last line 7 8, put A[6,7]=1  and A[7,6]=1
#Then calculate measures..
