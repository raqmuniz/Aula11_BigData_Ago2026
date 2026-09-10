def calcula_soma(x, y):
    return x + y


def calcula_subtracao(x,y):
    return x - y


def calcula_multiplicacao(x, y):
    return x * y

def calcula_divisao(x, y):
    return x / y 

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
print('\n####### Menu de opções #######')
print(30*'=')
print('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão')

opcao = int(input('\nEscolha a opção acima: '))

match opcao:
    case 1:
        operação = 'soma'
        resposta = calcula_soma(n1, n2)
    case 2:
        operação = 'Subtração'
        resposta = calcula_subtracao(n1, n2)
    case 3:
        operação = 'multipliação'
        resposta = calcula_multiplicacao(n1, n2)
    case 4:
        operação = 'divisão'
        resposta = calcula_divisao(n1, n2)
    case _:
        operação = "Inválida"
        resposta = 'Opção inválida'

print(f'Resultado: {operação} : {resposta}')
print('Fim')




