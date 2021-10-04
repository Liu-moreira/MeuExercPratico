# 6) Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até dez. Seu programa deverá
# ler um número pelo teclado (entre 0 e 10) e mostrá-lo por 
# extenso.


cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
'sete', 'oito', 'nove', 'dez')

while True:
    num = int(input('Digite um número de 0 a 10:'))
    if num >= 0 and num <= 10:
        break
print(f'O número digitado foi: {cont[num]}\n')
    