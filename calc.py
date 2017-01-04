import math

def C(n,r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

sum = 0
for i in range(0,7):    
    sum += C(6,i) * math.factorial(i + 1) * math.factorial(7-i)

for i in range(1,7):
    sum += C(6,i) * math.factorial(i) * math.factorial(8-i)

print( 4 * sum)
    