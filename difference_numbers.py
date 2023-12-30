numero_01 = int(input('Entre com o primeiro número: '))
numero_02 = int(input('Entre com o segundo número: '))
diferenca = numero_01 - numero_02
if diferenca > 0:
    print(f'{diferenca}')
else:
    diferenca = numero_02 - numero_01
    print(f'{diferenca}')
