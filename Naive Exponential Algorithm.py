
# Naive exponential algorithm ----- O(2^N)
    
import numpy as np
import time

def subsetSum(input_array, index):
    _sum = 0

    #calculate sum of the subset        
    for i in range(len(index)):
        #subset contains items that are marked 1
        if index[i] == 1:
            _sum = _sum + input_array[i]
    
    return _sum

def main():
    input_array = [2,4,1,6,7,3,9]
    n = len(input_array)
    flag = 0
    
    #required sum of subset in input array
    _sum = int(input("Enter the sum : "))
    
    #print("Total number of subsets = ", 1<<n)
    
    #iterating over 2^n subsets of the input array
    start_time = time.time()

    for i in range(1<<n):
        #using binary representation of each subset number to take or leave item
        index = list(map(int, np.binary_repr(i)))
       
        #padding the binary array with 0
        for j in range(n-len(index)):
            index[:0] = [0]
                    
        #calculate the sum based on the binary array
        result = subsetSum(input_array, index)
        
        #if sum of the subset = required sum then print the subset
        if result == _sum:
            flag = 1
            print("Subset :", end=" ")
            for j in range(len(index)):
                if index[j] == 1:
                    print(input_array[j], end = " ")
            break
    
    if flag == 0:
        print("No subset with sum",_sum)
        
        
    print("\n--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()