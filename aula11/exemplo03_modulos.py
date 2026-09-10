#Biblioteca
from modulos.operacoes import calcula_dobro, calcula_triplo, calcula_metade, calcula_quadrado
import random
import subprocess

#Essas funções foram retiradas deste arquivo para modularizar este código
#def calcula_dobro(x): #tanto faz a letra aqui, x será o mesmo valor de n
#    return x * 2


#def calcula_triplo(x):
#    return x * 3


#def calcula_quadrado(x):
 #   return x ** 2


#def calcula_metade(x):
#   return x / 2
#inicio
#n = int(input('Informe o número: '))
subprocess.run('cls', shell=True) #serve para limpar o terminal
n = random.randint(1, 10) #gera números aleatórios


print(f'número sorteado: {n}')
print('\n####### Menu de opções #######')
print(30*'=')
print('[1] - Dobro\n[2] - Triplo\n[3] - Quadrado')

opcao = int(input('\nEscolha uma opção acima: '))


match opcao:
    case 1:
        #dobro
       # total = n * 2
       # print(f'O dobro é: {total}')
        operação: 'Dobro'
        resposta = calcula_dobro(n)
    case 2:
        #triplo
       # total = n * 3
       # print(f'O triplo é: {total}')
        operação = 'Triplo'
        resposta = calcula_triplo(n)
    case 3:
        #quadrado
      #  total = n * n
      #  print(f'O quadrado é: {total}')
        operção = 'Quadrado'
        resposta = calcula_quadrado(n)
    case 4:
         operação = 'Metade'
         resposta = calcula_metade(n)
    case _:
        #opção inválida
        operação = 'Operação inválida'
        resposta = 'Opção inválida'

print(f'Resultado: {resposta}')
print('Fim')