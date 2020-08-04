real = float(input('Quanto dinheiro você tem? R$'))
cotacao = float(input('Qual a cotação atual do dolar? US$'))
dolar = real/cotacao

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))