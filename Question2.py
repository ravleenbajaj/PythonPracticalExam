t1=(1,2,5,7,9,2,4,6,8,10)

def printlines():
    length = int(len(t1)/2)
    print(t1[:length])
    print(t1[length:])

printlines()


def evenvals():
    l1 = []
    for i in t1:
        if i%2 == 0:
            l1.append(i)
        else:
            continue
    new_tuple = tuple(l1)
    print(new_tuple)

evenvals()


t2 = (11, 13, 15)
def concat_tuples():                              
    t3 = t1+t2
    print("New tuple: ", t3)

concat_tuples()

def minmax():
    t3 = t1+t2
    print("Minimum value in new tuple is : ", min(t3))
    print("Maximum value in new tuple is : ", max(t3))

minmax()