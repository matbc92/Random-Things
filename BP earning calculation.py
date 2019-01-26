# calculador de numero de battle points ganhos no battle maison do pokemon ORAS.
# O número de battle points ganhos começa em dois por batalha venida e aumenta em 1 por batalha a cada dez vitorias,
# e há uma excessão na batalha de numero 50 que da uma recompensa de 50 battle points ao ser vencida,
# a partir de 7 pontos por batalha vencida a recompensa para de aumentar.
while True:
    while True:
        try:
            batalhas = int(input('Número de batalhas vencidas:'))
            break
        except:
            print('Por favor digite somente o NÚMERO de batalhas vencidas')
    if batalhas == 0:
        print('Nenhum battle point ganho')
        break
    elif 1 < batalhas < 11:
        print('{} battle points ganhos:'.format(batalhas*2))
        break
    elif 11 < batalhas < 21:
        print('{} battle points ganhos:'.format(((batalhas-10))*3+(10*2)))
        break
    elif 21 < batalhas < 31:
        print('{} battle points ganhos:'.format(((batalhas-20)*4)+(10*2)+(10*3)))
        break
    elif 31 < batalhas < 41:
        print('{} battle points ganhos:'.format(((batalhas-30)*5)+(10*2)+(10*3)+(10*4)))
        break
    elif 41 < batalhas < 50:
        print('{} battle points ganhos:'.format(((batalhas-40)*6)+(10*2)+(10*3)+(10*4)+(10*5)))
        break
    elif batalhas == 50:
        print('{} battle points ganhos:'.format((10*2)+(10*3)+(10*4)+(10*5)+(9*6)+(50)))
        break
    elif batalhas > 50:
        print('{} battle points ganhos:'.format(((batalhas-50)*7)+(10*2)+(10*3)+(10*4)+(10*5)+(9*6)+(50)))
        break
    else:
        print('Não é possivel vencer menos do que nenhuma batalha, por favor digite um número coerente.')
