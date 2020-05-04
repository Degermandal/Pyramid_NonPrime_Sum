#If a number is a prime, return true.
def findPrime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

def findSum():
    pyramid =   [[1],
                [8, 4],
                [2, 6, 9],
                [8, 5, 9, 3]]

    sum = pyramid[0][0]
    i = 1
    j = 0
    while(i < len(pyramid)):
        if(findPrime(pyramid[i][j]) & findPrime(pyramid[i][j+1])):
            print("Both of them are prime number!")
            return
        else:
            if ( (pyramid[i][j] > pyramid[i][j+1]) & (findPrime(pyramid[i][j]) == False) ):
                sum += pyramid[i][j]
                j = j
            else:
                sum += pyramid[i][j+1]
                j = j+1
        i = i+1
    return sum

result = findSum()
print("Result: ", result)

