nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota da prova 1: '))
nota2 = float(input('Digite a nota da prova 2: '))
soma = nota1 + nota2
if soma != 0:
    media = (soma)/2
else:
    media = 0

print('{:=^50}'.format(' Start '))

print('Aluno: {}'.format(nome.capitalize()))
print('     - Prova 1: {:.2f}'.format(nota1))
print('     - Prova 2: {:.2f}'.format(nota2))
print('     # Média:   {:.2f}'.format(media))

print('{:=^50}'.format(' End '))