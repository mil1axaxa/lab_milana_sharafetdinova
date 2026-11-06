n=int(input('Введите число'))
x=1
step=4
while x<=n:
    x=x+step
    step=step+1
print('Первое число, большее n:',x)