# 6:
print('6:')
n: int = int(input('enter a number:'))
for i in range(n, 0, -1):
    print(i, end=',')
print('')

# 7:
print('7:')
x: int = int(input('enter a number:'))
y: int = int(input('enter a number:'))
if x % 2 == 0:
    for j in range(x, y + 1, 2):
        print(j, end=',')
else:
    for i in range(x + 1, y + 1, 2):
        print(i, end=',')
print('')
# 8:
print('8:')
n: int = int(input('enter a positive number:'))
for i in range(1, n + 1):
    if i % 5 == 0 or i % 3 == 0:
        print(i, end=",")
print('')

# 9:
print('9:')
n: int = int(input('enter a number:'))
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i, end=",")
print('')
