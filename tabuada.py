print('Tabuada')
# solicitar um número ao usuário
num = int(input('Digite um número de 1 a 10 para ver sua tabuada:'))

#verificar se o número está válido ao que foi pedido
if 1 <= num <= 10:
    print(f'\nTabuada de {num}:')
    #laço de repetição para calcular a tabuada
    for i in range(1,11):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')
else: 
    print('O número inserido deve ser de 1 a 10')