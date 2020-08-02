num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1 / 2)

print('{:=^50}'.format(' Start '))

print('O dobro de {} é {} \nO triplo é {} \nE a raíz quadrada é {:.2f}'.format(num, dobro, triplo, raiz))

print('{:=^50}'.format(' End '))