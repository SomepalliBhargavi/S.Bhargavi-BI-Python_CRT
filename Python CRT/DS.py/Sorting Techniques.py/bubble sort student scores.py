'''Sort Student Scores
You are given an array of integers representing student scores
Your task is to sort the array in ascending order using a basic sorting 
algorithm (Bubble Sort / Selection Sort/Insertion Sort)
Input
An integer n (1 sns 1000) number of students
An array of n integers the scores (8 1 score $ 100)'''

def bubble_sort(scores):
    for i in range(len(scores)):
        for j in range(len(scores)-i-1):
            if scores[j]>scores[j+1]:
                scores[j],scores[j+1]=scores[j+1],scores[j]
    print(f"Sorted scores: {scores}")
scores=[55,80,40,62,57,45]
print(f"unsorted scores: {scores}")
bubble_sort(scores)
