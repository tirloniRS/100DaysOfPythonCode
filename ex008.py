medida = float(input('Digite uma distância em metros: '))

km =  medida * 0.001
hm =  medida * 0.01
dam = medida * 0.1
dm =  medida * 10
cm =  medida * 100
mm =  medida * 1000

print('{:=^50}'.format(' Start '))

print('{:.0f}m equivale a: '.format(medida), end ='\n')
print( '{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm '.format(km, hm, dam, dm, cm, mm))

print('{:=^50}'.format(' Start '))
