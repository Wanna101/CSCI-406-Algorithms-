#Jasmine McCrary
#10864451

import sys

def dpT(segments):
    n = len(segments)
    dynamicP = [[(0, '')] * n for _ in range(n)] #2d list of lists that is initialized with tuples for max sum and order
    
    prefixSum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixSum[i] = prefixSum[i - 1] + segments[i - 1]
    
    #base case
    for i in range(n):
        dynamicP[i][i] = (segments[i], '')
    
    #dp table
    for segmentLength in range(2, n + 1):
        for i in range(n - segmentLength + 1):
            j = i + segmentLength - 1 #end index of segnment
            #bottom up process using prefix sums
            pickI = segments[i] + (prefixSum[j + 1] - prefixSum[i + 1] - dynamicP[i+1][j][0])
            pickJ = segments[j] + (prefixSum[j] - prefixSum[i] - dynamicP[i][j-1][0])
            
            #decision to pick which segment
            if pickI >= pickJ:
                dynamicP[i][j] = (pickI, 'L')
                
            else:
                dynamicP[i][j] = (pickJ, 'R')
                
            #dynamicP[i][j] = max(pickI, pickJ)
            
    return dynamicP[0][n-1][0], dynamicP

#traceback function
def traceback(dynamicP, segments):
    i, j = 0, len(segments) - 1
    order = [] #stores the order of segments being picked
    
    #loops through the whole range of segments and checks if the optimal choice was picked
    while i <= j:
        if dynamicP[i][j][1] == 'L':
            order.append(i+1)
            i += 1
        else:
            order.append(j+1)
            j -= 1
        
    return order
    

#testing
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        segments = list(map(int, lines[1].strip().split()))
        
    max_value, dynamicP = dpT(segments)
    order = traceback(dynamicP, segments)
    print(max_value)
    print(" ".join(map(str, order)))