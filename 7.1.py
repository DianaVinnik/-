a = int(input("Введите целое число: "))
a = str(a)

count = 0

for x in range(10):
    print('Колличество цифр', x, 'в числе =', a.count(str(x)))

