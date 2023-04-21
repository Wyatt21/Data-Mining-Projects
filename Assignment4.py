import numpy as numpy
from math import sqrt
import random
from scipy.stats import norm


irisFile = "C:/Users/wyatt/Desktop/Assignment4/iris.txt"
iris_data = numpy.loadtxt(irisFile,dtype=float,delimiter=' ')



fourCirclesFile = "C:/Users/wyatt/Desktop/Assignment4/fourCircles.txt"
fourCircles_data = numpy.loadtxt(fourCirclesFile,dtype=float,delimiter=' ')

t48kFile = "C:/Users/wyatt/Desktop/Assignment4/t4.8k.txt"
t48k_data = numpy.loadtxt(t48kFile,dtype = float, delimiter = ' ')

twoCircleFile = "C:/Users/wyatt/Desktop/Assignment4/twoCircles.txt"
twoCircles_data = numpy.loadtxt(twoCircleFile,dtype = float, delimiter = ' ')

twoEllipsesFile = "C:/Users/wyatt/Desktop/Assignment4/twoEllipses.txt"
twoEllipses_data = numpy.loadtxt(twoEllipsesFile,dtype = float, delimiter = ' ')



##Function that calculates the euclidean distance between two points
def euclidean_distance(point1, point2):
    return (sqrt(numpy.sum(numpy.power((point1-point2),2))))

def k_means_clustering(data, k):
    
    iterations = 0
    max_iterations = 20 #Maximum amount of iterations
    epsilon = 0.00000000001
    delta = 1
    final_clusters = [[0]] * 3
    
    numberOfPoints = data.shape[0] #Number of points in data
    numberOfRows = data.shape[1] #Number of demensions in data
    
    randomIds = random.sample(range(numberOfPoints),k)
    centroids = data[randomIds,:]
    old_averages = sum(sum(centroids))
    while iterations < max_iterations and delta > epsilon:
        indices = []
        new_averages = [0] * numberOfRows
        numbers = [0] * k
        for i in range(numberOfPoints):
            point = data[i,:]
            distances = [0] * k
            for j in range(k):
                distance = euclidean_distance(point, centroids[j,:])
                distances[j] = distance
            minDistance = min(distances)
            ids = distances.index(minDistance)
            indices.append(ids)
        for i in range(k):
            total = 0
            sums = [0] * numberOfRows
            for j in range(numberOfPoints):
               point = data[j,:]
               if(indices[j] == i):
                   total = total + 1
                   
                   for x in range(numberOfRows):
                       sums[x] = sums [x] + point[x]
            for j in range(numberOfRows):
                new_averages[j] = sums[j] / total
            centroids[i] = new_averages
        iterations = iterations + 1
    for i in range(k):
        print("cluster ",i,  "with centroid: ", centroids[i])
        for j in range(numberOfPoints):
            if(indices[j] == i):
                print(data[j,:])
        
k_means_clustering(iris_data, 3)


























