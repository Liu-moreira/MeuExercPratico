# 4) Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.


listadepesos = []
for contagem in range(1, 6):
    peso = float(input(f'Insira o peso da {contagem}ª pessoa: '))
    listadepesos.append(peso)

print(f'O menor peso lido foi: {min(listadepesos)}')  # Menor item da lista
print(f'O maior peso lido foi: {max(listadepesos)}')  # Maior item da lista