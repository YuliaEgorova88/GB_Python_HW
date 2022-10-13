n = int(input('Введите число N: '))

summ = 0
for num in range(1, n + 1):
    if num % 2 == 0:
        print(num)
        summ += num

print(f'\n{summ}')        