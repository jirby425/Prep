
def sockMerchant(n, ar):
    if n < 2:
        return 0

    ar.sort()
    count = 0
    i = 0
    while i in range (0, n-1):
        if (ar[i] == ar[i+1]):
            count = count + 1
            i = i + 2
        else:
            i = i + 1
    return count

if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    print result
