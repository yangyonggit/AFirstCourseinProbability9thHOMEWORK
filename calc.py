import math

def C(n,r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))


# 1.30
sum = 0
for i in range(0,7):    
    sum += C(6,i) * math.factorial(i + 1) * math.factorial(7-i) 

for i in range(1,7):
    sum += C(6,i) * math.factorial(i) * math.factorial(8-i)

print( 4 * sum)

# 1.31*

def h(n,r):
    if (r == 1):
        return 1
    elif(r == 2):
        return C(n-1,1)
    else:
        s = 0
        for i in range(1,n-1):
            s += h(n-i,r-1)
        return s

print(h(8,4))
sum = 0 
for i in range(1,5):
    sum += C(4,i) * h(8,i)
print(sum)


# 1.32*
def zh(n,r):
    s = 0
    for i in range(1,r+1):
        s += C(r,i) * h(n,i)
    return s


print zh(8,6)

print zh(5,6) * zh(3,6)
# b

