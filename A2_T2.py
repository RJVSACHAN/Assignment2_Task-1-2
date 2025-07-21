# Task 2: Sum of Integers from 1 to 50 Using for Loop
'''Sum = 0
for i in range(1, 51):
    Sum += i
print(f'The sum of numbers from 1 to 50 is: {Sum}')'''

Sum = 0
a=int(input('Enter the first number: '))
b=int(input('Enter the last number: '))
for i in range(a, b+1):
    Sum += i
print(f'The sum of numbers from {a} to {b} is: {Sum}')