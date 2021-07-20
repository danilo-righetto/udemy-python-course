"""
Condições IF, ELSEIF e ELSE
"""
altura = 1.70
peso = 85.7
imc = peso / (altura ** 2)
if imc > 20:
    print(f'O IMC {imc} é maior que 20.')
elif imc < 20:
    print(f'O IMC {imc} é menor que 20.')
else:
    print(f'O seu IMC é 20.')