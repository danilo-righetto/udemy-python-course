"""
Entrada de dados com Python
"""
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
ano_nascimento = 2021 - int(idade)

print(f'O usuario digitou {nome} e o tipo da variavel é: {type(nome)}.')
print(f'O usuario {nome} tem {idade} anos.')
print(f'O usuario {nome} nasceu em {ano_nascimento}.')

primeiro_numero = input("Digite um numero: ")
segundo_numero = input("Digite outro numero: ")
resultado = int(primeiro_numero) + int(segundo_numero)
print(f'O resultado da soma dos dois numero é {resultado}')