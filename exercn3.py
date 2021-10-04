# 3) Crie um programa que solicite um número entre 1 e 10. Se a
# pessoa digitar um número diferente, deve mostrar a mensagem
# "Entrada inválida" e solicitar o número novamente.
# Se digitar correto, mostrar o número digitado.


while True:
    n = int(input('Informe um número entre 1 e 10: '))
    if n >= 1 and n <= 10:
        print(n)
        break
    else:
        print('Entrada inválida!')