"""
* Criar variaveis para nome, idade, altura e peso de uma pessoa
* Criar uma variavel com o ano atual
* Obter o ano de nascimento de uma pessoa
* Obter o IMC de uma pessoa com duas casas decimais (peso e altura)
* Exibir um texto com todos os valores na tela usando F-Strings (com chaves)
"""

nome = 'Joao Carlos'
idade = 27
altura = 1.70
peso = 85.7
imc = peso / (altura ** 2)
ano_atual = 2021
data_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {data_nascimento}')