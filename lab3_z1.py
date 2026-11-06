n=int(input('Введите число'))
f=False
for x in range(1,n+2):
    s=x**2
    if s>n and not f:
        print('Первое число, большее n:', s)
        f=True