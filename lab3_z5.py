A=[]
B=[]
print('Введите 10 элементов массива А:')
for i in range(10):
    A.append(float(input(f'A[{i}] = ')))

print('Введите 10 элементов массива B:')
for i in range(10):
    B.append(float(input(f'B[{i}] = ')))

print('Исходный A:',A)
print('Исходный B:',B)
A,B=B,A
print('Новый A:',A)
print('Новый B:',B)