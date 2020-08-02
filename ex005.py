n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

Soma = n1 + n2
produto = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
resto_da_divisao = n1 % n2
potencia = n1 ** 2


print('{:=^50}'.format(' Start '))

print('Primeiro número: {}'.format(n1))
print('Segundo número: {}'.format(n2))
print('A soma é {}'.format(Soma))
print('O produto é {}'.format(produto))
print('A divisão é {}'.format(divisao))
print('A divisão comn duas casas decimais é {:.2f}'.format(divisao))
print('A divisão inteira é {}'.format(divisao_inteira))
print('O resto da divisão é {}'.format(resto_da_divisao))
print('O quadrado do primeiro numero é {}'.format(potencia))

print('{:=^50}'.format(' End '))
