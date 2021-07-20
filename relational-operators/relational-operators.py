"""
Operadores Relacionais
== > >= < <= !=
"""

print('Igualdade:', 2 == 2)
print('Maior:', 5 > 4)
print('Maior ou igual:', 8 >= 7)
print('Menor:', 8 < 9)
print('Menor ou igual:', 10 <= 11)
print('Diferente:', 12 != 14)

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

if idade >= 22:
    print(f'{nome} poderá pegar um empréstimo')
elif idade < 22:
    print(f'{nome} não poderá fazer empréstimos.')