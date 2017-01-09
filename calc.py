import math

def C(n,r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

def P(n):
    return math.factorial(n)


# 1.30
sum = 0
for i in range(0,7):    
    sum += C(6,i) * math.factorial(i + 1) * math.factorial(7-i) 

for i in range(1,7):
    sum += C(6,i) * math.factorial(i) * math.factorial(8-i)

print( 4 * sum)
print('---------------------------')

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
print('---------------------------')

# 1.32*
def zh(n,r):
    s = 0
    for i in range(1,r+1):
        s += C(r,i) * h(n,i)
    return s


print zh(8,6)

print zh(5,6) * zh(3,6)

print('---------------------------')

# 1.33*
print('1.33*')
print(zh(9,4))
print(zh(9,4) + zh(13,3) + zh(12,3) + 2 * zh(11,3))

print('---------------------------')


# THEORETICAL EXERCISES
# 6
def func6(n,r):
    if (r==1):
        return n
    else:
        s = 1
        for i in range(1,n-r+1):
            s += func6(n-i,r-1)
        return s
    

print(func6(6,3))



# SELF-TEST PROBLEMS AND EXERCISES
print("SELF-TEST PROBLEMS AND EXERCISES")
# 1
print("PROBLEMS 1")
print(2*P(5))
print(P(6) / 2)
print(P(6) / 6)
print(P(6) / 4)
print(P(4) * 2 * 2)
print(P(6) - P(5))


#2
print("PROBLEMS 2")
print(P(4)*P(3)*P(3)*P(3))

#3
print("PROBLEMS 3")
print(10 * 9 * 8)
print(8*7*6 + C(2,1)*C(3,1)*8*7)
print(8*7*6 + 8*P(3))
print(C(3,1) * 9 * 8)
print(9*8 + 9*8*7)

#4
print("PROBLEMS 4")
print(C(10,7))
print(C(5,3)*C(5,4) +  C(5,4)*C(5,3) + C(5,5)*C(5,2))

#5
print("PROBLEMS 5")
print(P(7) / (P(3) * P(2) * P(2)))

#6
print("PROBLEMS 6")
print(pow(26,3) * pow(10,4))

#10
print("PROBLEMS 10")
print(pow(9,5))
print(9*8*7*6*5 + C(9,1)* C(5,2) * 8 * 7 *6 + C(9,2) * 7 * P(5) / (P(2) * P(2)))

#11
print("PROBLEMS 11")
s = 0
for i in range(0,7):    
    s+=C(10,i)*C(10 - i,6 - i)
print(s)
print(C(10,3) * C(7,3))

#print(C(10,6) * pow(2,6))
#print(P(10) / (P(3) * P(3) * P(4)))

#12
print("PROBLEMS 12")
print(C(7,2) * C(8,3))

#16
print("PROBLEMS 16")
s = 0
for i in range(1,5):
    s+=C(5,i) + C(15,4-i)
print(s)


#18
print("PROBLEMS 18")
s = 3+6+10+7*2*2+6*2*3
print(s)

