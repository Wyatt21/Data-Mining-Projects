import numpy
from math import sqrt

##Function that calculates the euclidean distance between two points
def euclidean_distance(point1, point2):
    return (sqrt(numpy.sum(numpy.power((point1-point2),2))))

pcTrainingFile = "C:/Users/wyatt/Desktop/Assignment2/irisPCtraining.txt"
pcTraining_data = numpy.loadtxt(pcTrainingFile,dtype=float,delimiter=' ')

pcTestingFile = "C:/Users/wyatt/Desktop/Assignment2/irisPCtesting.txt"
pcTesting_data = numpy.loadtxt(pcTestingFile,dtype=float,delimiter=' ')

trainingFile = "C:/Users/wyatt/Desktop/Assignment2/irisTesting.txt"
training_data = numpy.loadtxt(trainingFile,dtype=float,delimiter=' ')

testingFile = "C:/Users/wyatt/Desktop/Assignment2/irisTesting.txt"
testing_data = numpy.loadtxt(testingFile,dtype=float,delimiter=' ')



def k_nearest(k, training, testing):
    
    n = int(training.shape[0]) #amount of points in training
    training_index_of_labels = int(training.shape[1]-1) #index of the labels
    testing_index_of_labels = int(testing.shape[1]-1)
    tp = 0 #True Positive
    fp = 0 #False Positive
    tn = 0 #True Negative
    fn = 0 #False Negative
    testing_points = testing[:,:testing_index_of_labels]
    
    length = int(testing.shape[0]) #amount of points in the testing data
    temp= [] #temp list
    predicted_label = 0.0 #temp variable to hold the predicted label
    k_smallest_labels= [] #temp list to hold the k smallest labels from the training data
    
    for i in range(length):
        for j in range(n):
            temp_distance = euclidean_distance(testing_points[i,:], training[j,:training_index_of_labels]) #temp_distance is equal to the distance between 
            temp.append([training[j], temp_distance]) #adds a list of the training point and the distance between the testing and training points to temp
        temp = sorted(temp, key=lambda x: x[1], reverse=False) #sorts temp by distance in ascending order
        for j in range(k):
            k_smallest_labels.append(temp[j][0][training_index_of_labels]) #adds the labels of the k-smallest distances to a list
        
        total = sum(k_smallest_labels) #sum of the labels
        
        #if the sum of the labels is >0 then the majority is 1 and if it <0 then the majority is -1
        if total > 0:
            predicted_label = 1.0
        if total == 0:
            predicted_label = 1.0
        if total < 0:
            predicted_label = -1.0
        
        #Increments tp, fp, tn, fn
        if predicted_label == 1.0 and testing[i][testing_index_of_labels] == 1.0:
            tp = tp + 1
        if predicted_label == 1.0 and testing[i][testing_index_of_labels] == -1.0:
            fp = fp + 1
        if predicted_label == -1.0 and testing[i][testing_index_of_labels] == -1.0:
            tn = tn + 1
        if predicted_label == -1.0 and testing[i][testing_index_of_labels] == 1.0:
            fn = fn + 1
            
        k_smallest_labels.clear()
        temp.clear()
       
    accuracy = (tp + tn)/(tp + fp + tn + fn)
    sensitivity = tp/(tp + fn)
    specificity = tn/(fp + tn)
    precision = tp/(tp+fp)
    
    print ('tp: ' , tp)
    print ('fp: ' , fp)
    print ('tn: ' , tn)
    print ('fn: ' , fn)
    print('accuracy: ', accuracy)
    print('sensitivity: ', sensitivity)
    print('specificity: ', specificity)
    print('precision: ', precision)

#k = 5,10,20 for PC and non PC data
print('k = 5 for iris training and iris testing')
k_nearest(5, training_data, testing_data)
print('')
print('k = 10 for iris training and iris testing')
k_nearest(10, training_data, testing_data)
print('')
print('k = 20 for iris training and iris testing')
k_nearest(20, training_data, testing_data)
print('')
print('k = 5 for irisPC training and iriesPC testing')
k_nearest(5, pcTraining_data, pcTesting_data)
print('')
print('k = 10 for irisPC training and iriesPC testing')
k_nearest(10, pcTraining_data, pcTesting_data)
print('')
print('k = 20 for irisPC training and iriesPC testing')
k_nearest(20, pcTraining_data, pcTesting_data)















