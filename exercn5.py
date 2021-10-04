# 5) Usando o nome dos seus colegas Aline, Bruna, Gustavo, Huan,
# Marlon, Rafa, Rafael e Victor, faça um programa que leia os
# nomes e sortei um deles para responder a próxima questão, 
# escrevendo na tela o nome do escolhido.


lista = ['Aline', 'Bruna', 'Gustavo', 'Huan', 'Marlon', 'Rafa', 'Rafael', 'Victor']

import random
escolhido = random.choice(lista)
print(f'\n O escolhido para responder a próxima questão foi: {escolhido} \n')



# # OUTRA FORMA:
# from random import choice
# escolhido = choice(lista)
# print(f'\n O escolhido para responder a próxima questão foi: {escolhido} \n')