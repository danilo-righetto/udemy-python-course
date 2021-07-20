"""
Operador Lógicos - and, or, not, in, not in
"""

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

# Limite para pegar emprestimo
idade_menor = 20 # Muito jovem
idade_maior = 30 # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} não poderá pegar o emprestimo.')

if 'a' in nome:
    print(f'No nome {nome} existe a letra "a".')
else:
    print(f'No nome {nome} não existe a letra "a".')

if 'b' not in nome:
    print(f'No nome {nome} existe a letra "b".')
else:
    print(f'No nome {nome} não existe a letra "b".')