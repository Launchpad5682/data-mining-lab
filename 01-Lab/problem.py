#!/usr/bin/python3

# To implement vectors, lists, matrices, arrays, factors, dataframes, 
# different operators, and data structures

# Python operators
# Arithmetic operator

# Addition 
sum = 10 + 20
print("10+20 = ",sum)

# Subtraction
sub = 20 - 10
print("20-10 = ",sub)

# Multiplication 
mul = 10*20
print("10*20 = ",mul)

# Division
div = 20/5
print("20/5 = ",div)

# Modulus
mod = 121%5
print("121%5 = ",mod)

# Exponentiation
exp = 10**2
print("10**2 = ",exp)

# Floor division 
floor = 21//5
print("21//5 =  ", floor)

# Assignment operator
x = 5 
print("x=",5)

# x = x + 3
x += 3
print("x+=3: ",x)

# x = x - 2
x -= 2
print("x-=2: ",x)

# x = x * 2
x *= 2
print("x*=2: ",x)

# x = x / 2
x /= 2
print("x/=2: ",x)

# x = x % 3
x %= 3
print("x%=3: ",x)

x = 10
print("x: ",x)

# x = x // 3
x //= 2
print("x//=2: ",x)

# x = x ** 2
x **= 2
print("x**=2: ",x)

x = 0
# x = x & 1
x &= 1
print("x&=1: ",x)

# x = x | 1
x |= 1
print("x|=1: ",x)

# x = x ^ 3
x ^= 3
print("x^=3: ",x)

# x = x >> 3
x >>= 3
print("x>>=3: ",x)

# x = x << 3
x <<= 3
print("x<<=3: ",x)

# Comparision operator
# Equal 
print("2 == 2: ",2==2)
print("2 == 1: ",2==1)

# Not equal
print("2 != 2: ",2!=2)
print("2 != 1: ", 2!=1)

# Greater than 
print("10 > 2: ",10>2)
# Less than 
print("10 < 2: ",10<2)

# Greater equal
print("2 >= 2: ", 2>=2)

# Less than
print("-1 <= 10: ", -1 <= 10)

# Logical operator
x = 4
print("x<5 and x<10: ", x<5 and x<10)
print("x<5 or x<2: ", x<5 or x<4)

print("not(x<5 anf x<10): ",not(x<5 and x<10))

# Identity operator
x = 5
y = x
print("x is y: ", x is y)
print("x is not y: ", x is not y)

# Membership operator
cubes = {x: x * x * x for x in range(10)}

print("27 in cubes: ", 27 in cubes)
print("18 not in cubes: ", 18 not in cubes)

# Bitwise operator
print("1 & 1: ", 1 & 1)
print("1 | 0: ", 1 | 0)
print("1 ^ 0: ", 1 ^ 0)
print("~1: ", ~1)
print("2 << 1: ", 2 << 1)
print("2 >> 1: ", 2 >> 1)

# dictionary
# key value pair
cubes = {x: x * x * x for x in range(10)}

print("Cubes of numbers from 0 to 9:")
print(cubes)

# list 
array = [x for x in range(10)]
print(array)

array.append(10)
print(array)
print(type(array))

# tuple
arr = (1,2,3,4,5,6,7,8,9,10)
print(arr)
print(type(arr))
