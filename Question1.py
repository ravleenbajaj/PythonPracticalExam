def oddsum():
    n= int(input("Enter the number of terms:"))
    sum=0
    for i in range (1, 2*n+1, 2):
        sum += i
    print("The sum of first", n, "odd terms is:", sum)



def evensum():
    n= int(input("Enter the number of terms:"))
    sum=0
    for i in range (0, 2*n+1, 2):
        sum += i
    print("The sum of first", n, "even terms is:", sum)



def sumodd(n):
    return (n * n)

def sumeven(n):
     return (n * (n + 1))

def findSum(num):

    sumo = 0
    sume = 0
    x = 1
    cur = 0
    ans = 0
    while (num > 0):
        inc = min(x, num)
        num -= inc
        if (cur == 0):
            ans = ans + sumodd(sumo + inc) - sumodd(sumo)
            sumo += inc
        else:
            ans = ans + sumeven(sume + inc) - sumeven(sume)
            sume += inc
        x *= 2
        cur ^= 1
    return ans

n = int(input("Enter number of terms:"))
print("The sum of first n terms is:", findSum(n))