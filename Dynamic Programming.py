#!/usr/bin/env python
# coding: utf-8

S = [1,3,6]
T = 5


S = [3, 34, 4, 12, 5, 2] 
T = 9


S = [2, 3, 5, 6, 8] 
T = 10



n = len(S)
subset_matrix = [[False for i in range(T+1)]  for j in range(n+1)]

for i in range(n+1): 
    subset_matrix[i][0] = True

for i in range(1,n+1): 
    for j in range(1,T+1): 
        if S[i-1] > j: 
            subset_matrix[i][j] = subset_matrix[i-1][j] 
        else: 
            subset_matrix[i][j] = (subset_matrix[i-1][j] or subset_matrix[i - 1][j-S[i-1]]) 
 


subset_matrix[n][T]



printSet = [0]
printSet.extend(S)
print("\t",end='')
for i in range(T + 1):
    print(i, end='\t')
print()
for i in range(n+1):
    print(printSet[i], end='\t')
    for j in range(T + 1): 
        print (subset_matrix[i][j], end='\t') 
    print() 



if subset_matrix[n][T] == False:
    print("No solution possible")
else:
    print(findSubset(subset_matrix, n, T, [])[1:])




def findSubset(subset_matrix, n, T, subset):
    if T == 0:
        return [0]
    else: 
        while subset_matrix[n][T] == True:
            n = n-1
        n = n + 1
        subset = findSubset(subset_matrix, n, T - S[n-1] , subset)
        subset.append(S[n-1])
        return subset




