# To do this algorithm with the BONUS. I have to use Joe Marini explanation and algorithm combined with a simple sorting algorithm that I figure out myself. 
# Thanks to this challengue, I am learning about recursion and mergesort algorithm. I know that this algorithm can be improved and that QuickSort is the best, 
# but I am learning, so I have to grasp this concept very well. What was difficult to me was the use of a double recursion. Can anyone help me and correct my mistake. 
# Please like and comment.
# Date of last modification: 5-29-2019

import numpy as np

#Joe Marini wrote this part...I debugged and understood the concept in a 60%
def mergeSortPerArray(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recursively break down the arrays
        mergeSortPerArray(leftarr)
        mergeSortPerArray(rightarr)
        
        dataset= mergeTwoArrays(leftarr,rightarr,dataset)

        # while both arrays have content


# This was wrote by me and it is just a simple sorting algorithm. 
def mergeTwoArrays(firstArray, secondArray, dataset):

        # now perform the merging
    i=0 # index into the left array
    j=0 # index into the right array
    k=0
    
    while  i< len(firstArray) and j < len(secondArray) :
        if (firstArray[i] < secondArray [j]):
            dataset[k] = firstArray[i]
            i += 1
        else:
            dataset[k]= secondArray[j]
            j += 1
        k += 1
    
    while i< len(firstArray):
        dataset[k]= firstArray[i]
        i += 1
        k += 1 

    while j< len(secondArray):
        dataset[k]= secondArray[j]
        j += 1 
        k += 1

    return dataset
    
   



#First array
firstArray=list(map(int,input("Enter your first array. Each number must be separated by using a comma:\n").split(',')))
mergeSortPerArray(firstArray)
print(firstArray)
#Second Array
secondArray=list(map(int,input("Enter your second array. Each number must be separated by using a comma:\n").split(',')))
mergeSortPerArray(secondArray)
print(secondArray)
finalArray =np.empty(len(firstArray)+len(secondArray), int)
finalArray = mergeTwoArrays(firstArray, secondArray, finalArray)
print(finalArray)