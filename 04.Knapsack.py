import sys

def knapsack(v, w, n, W):

    if W < 0:
        return -sys.maxsize
    if n < 0 or W == 0:
        return 0
    include = v[n] + knapsack(v, w, n - 1, W - w[n])
    exclude = knapsack(v, w, n - 1, W)
    return max(include, exclude)
    
if __name__ == '__main__':
    v = [50,22,36,41,22,33]
    w = [3,5,6,4,7,2,3,1]
    W = 20
 
    print("Knapsack value is", knapsack(v, w, len(v) - 1, W))