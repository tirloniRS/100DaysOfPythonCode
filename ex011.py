l = float(input('Quantos metros de largura tem sua parede?'))
a = float(input('Quantos metros de altura tem sua parede?'))

area = l * a
tinta = area / 2
print('Sua parede tem a dimensão de {}x{}, e sua área é de {:.2f}m²'.format(l, a, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))
