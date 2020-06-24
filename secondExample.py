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
    pyramid =   [[215],
                [193, 124],
                [117, 237, 442],
                [218, 935, 347, 235],
                [320, 804, 522, 417, 345],
                [229, 601, 723, 835, 133, 124],
                [248, 202, 277, 433, 207, 263, 257],
                [359, 464, 504, 528, 516, 716, 871, 182],
                [461, 441, 426, 656, 863, 560, 380, 171, 923],
                [381, 348, 573, 533, 447, 632, 387, 176, 975, 449],
                [223, 711, 445, 645, 245, 543, 931, 532, 937, 541, 444],
                [330, 131, 333, 928, 377, 733,  17, 778, 839, 168, 197, 197],
                [131, 171, 522, 137, 217, 224, 291, 413, 528, 520, 227, 229, 928],
                [223, 626,  34, 683, 839,  53, 627, 310, 713, 999, 629, 817, 410, 121],
                [924, 622, 911, 233, 325, 139, 721, 218, 253, 223, 107, 233, 230, 124, 233]
             ]

    sum = pyramid[0][0]
    i = 1
    j = 0
    while(i < len(pyramid)):
        if(findPrime(pyramid[i][j]) & findPrime(pyramid[i][j+1])):
            print("Both of them are prime!!")
            return sum
        else:
            if ( (pyramid[i][j] > pyramid[i][j+1]) & (findPrime(pyramid[i][j]) == False) ):
                sum += pyramid[i][j]
                print("Sum1:", sum, "- the number:", pyramid[i][j])
                j = j
            else:
                sum += pyramid[i][j+1]
                print("Sum2:", sum, "- the number:", pyramid[i][j+1])
                j = j+1
        i = i+1

    return sum

result = findSum()
print("Result: ", result)

