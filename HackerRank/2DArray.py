import math

def hourglassSum(arr):

    max = float("-inf")
    for i in range(1,len(arr)-1):
        for j in range(1, len(arr[0])-1):
            sum = sumHelp(i,j,arr)
            print sum
            if sum > max:
                max = sum

    return max

def sumHelp(i,j,arr):
    sum = arr[i][j] + arr[i-1][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
    return sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []


    arr.append([1, 1, 1, 0, 0, 0])
    arr.append([0, 1, 0, 0, 0, 0])
    arr.append([1, 1, 1, 0, 0, 0])
    arr.append([0, 0, 2, 4, 4, 0])
    arr.append([0, 0, 0, 2, 0, 0])
    arr.append([0, 0, 1, 2, 4, 0])

    print arr


    result = hourglassSum(arr)
    print result

    #fptr.write(str(result) + '\n')

    #tr.close()
