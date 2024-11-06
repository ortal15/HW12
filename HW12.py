# 1:
print('1:')

x: float = float(input('enter a number:'))

print(f'{x - 10 if x > 10 else x * 10}')

# 2:
print('2:')
num1: float = float(input('enter a number:'))
num2: float = float(input('enter a second number:'))
num3: float = float(input('enter a third number:'))
amount: float = num1 + num2 + num3
print(f'{amount if amount > 100 else "The amount is less than 100"}')

# 3:
print('3:')
input1: float = float(input('enter a number:'))
input2: float = float(input('enter a number:'))
print(
    f'the input {'1 is bigger' if input1 % 1 > input2 % 1 else ('2 is bigger' if input1 % 1 < input2 % 1 else 'equal')}')

# 4:
print('4:')
age: int = int(input('enter your age:'))
if age >= 120 or age <= 0:
    print("Incorrect age.")
else:
    print(f'your age is {age}')

# 5:
print('5:')
number: int = int(input('enter a three-digit number:'))
x = number // 10
result = x % 10
print(f'the middle digit is: {result}')
