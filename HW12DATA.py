# 11:
print('11:')

neg: int = 0
while True:
    x: int = int(input('enter a number:'))
    if x < 0:
        neg += x
        continue
    elif x == 0:
        break
print(neg)

# 12:
print('12:')
list12: list[int] = [int(input('enter a number:')) for i in range(10)]
print(list12[::-1])

# 13
print('13:')
prime_count = 0
while True:
    number = int(input('enter a number:'))
    if number == 0:
        break

    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        prime_count += 1

print(f'{prime_count} numbers are prime')

# 14:
print('14:')
numbers: list[float] = []

for i in range(5):
    number = float(input('enter a number:'))
    numbers.append(number)

average = sum(numbers) / len(numbers)

count_above_average = sum(1 for number in numbers if number > average)

print(f"the average is: {average}")
print(f"the numbers that bigger then the average {count_above_average}")

print('15:')
quotient: int = 0
dividend: int = int(input('enter a number bigger than 0:'))
divisor: int = int(input('enter a number bigger than 0:'))

while dividend >= divisor:
    dividend -= divisor
    quotient += 1

print(f"The result of the complete division is:{quotient}")
print(f"The remainder is:{dividend}")
