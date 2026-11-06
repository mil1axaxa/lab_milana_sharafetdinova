n=int(input('Введите число'))
mas=[]
print('Введите элементы массива:')
for i in range(n):
    element=int(input(f'Элемент {i+1}:'))
    mas.append(element)
min_abs=abs(mas[0])
min_element=mas[0]
for x in mas:
    if abs(x)<min_abs:
        min_abs=abs(x)
        min_element=x
print('Минимальный элемент в списке:', min_element)
print('Массив в обратном порядке:')
for i in range(n-1,-1,-1):
    print(mas[i],end='')
print()
