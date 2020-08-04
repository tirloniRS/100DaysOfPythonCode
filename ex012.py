preco = float(input('Qual o preço do produto? R$'))
novo_preco = preco - preco * 0.05

print('O produto que custava R${:.2f}, na promoção dom desconto de 5%, vai custar apenas R${:.2f}'.format(preco, novo_preco))
