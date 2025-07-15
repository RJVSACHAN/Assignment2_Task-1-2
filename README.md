# Solution of Assignment 2: Module 3: Control Structures in Python
# Check for even and odd number
a=int(input('Enter the number: '))
b=a%2
if b==0:
    print(f'{a} is an Even number.')
else:
    print(f'{a} is an Odd  number.')

# sum of numbers in a given range
# Task 2: Sum of Integers from 1 to 50 Using for Loop
Sum = 0
for i in range(1, 51):
    Sum += i
print(f'The sum of numbers from 1 to 50 is: {Sum}')

# Task 2: Sum of Integers from 1 to 50 Using for Loop
'''Sum = 0
for i in range(1, 51):
    Sum += i
print(f'The sum of numbers from 1 to 50 is: {Sum}')'''

# Task 2: Sum of Integers between two numbers Using for Loop
Sum = 0
a=int(input('Enter the first number: '))
b=int(input('Enter the last number: '))
for i in range(a, b+1):
    Sum += i
print(f'The sum of numbers from {a} to {b} is: {Sum}')
