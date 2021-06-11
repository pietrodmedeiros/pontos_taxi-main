
import csv
csvfile = open('pontos_taxi.csv', encoding="utf8")
array = csv.reader(csvfile, delimiter=';', quotechar=';')

menu = ('========================================\n|           Pontos de taxi POA         |\n==================MENU================== \n  1. Listar todos os pontos de taxi \n  2. Informar localização \n  3. Encontrar pontos próximos \n  4. Buscar pontos por logaradouro \n  5. Fechar o pograma')



print(menu)

resp = input('Escolha a opção desejada:\n  ')

def listarPontos():
    for row in array:
        if (row[3] == ''):
            print(' Nome do ponto: ' + row[2] + '\n Telefone: Telefone não cadastrado'  + '\n Endereço: ' + row[4] + row[5] + '\n\n')
        else:
            print(' Nome do ponto: ' + row[2] + '\n Telefone: ' + row[3] + '\n Endereço: ' + row[4] + row[5] + '\n\n')
        
    voltar = input('Voltar ao Menu? [S/N] \n').upper()
    if (voltar == 'S'):
        print(menu)
        resp = input('Escolha a opção desejada:\n  ')
    elif (voltar == 'N'):
        print('Programa encerrado! \n\n\n')
    else:
        print('Valor inválido. Por favor insira um valor válido.')    


def informarLoc():
    print(' ')
    long = input('Digite a longitude: \n  ')
    lat = input('Digite a latitude \n  ')
    print(long + lat)
    voltar = input('Voltar ao Menu? [S/N] \n')
    if (voltar == 'S'):
        print(menu)
        resp = input('Escolha a opção desejada:\n  ')
    elif (voltar == 'N'):
        print('Programa encerrado! \n\n\n')
    else:
        print('Valor inválido. Por favor insira um valor válido.') 

def encontrarPontos():
    print('Listar os 3 pontos mais próximos')
    voltar = input('Voltar ao Menu? [S/N] \n')
    if (voltar == 'S'):
        print(menu)
        resp = input('Escolha a opção desejada:\n  ')
    elif (voltar == 'N'):
        print('Programa encerrado! \n\n\n')
    else:
        print('Valor inválido. Por favor insira um valor válido.') 

def buscarLog():
    log = input('Digite o logradouro ou parte dele: \n  ').upper()
    
    for row in array:
        if (row[4] == log):
            print(' Nome do ponto: ' + row[2] + '\n Endereço do ponto: ' + row[4] + ' ' + row[5] + '\n')

    print(' ')
    voltar = input('Voltar ao Menu? [S/N] \n')
    if (voltar == 'S'):
        print(menu)
        resp = input('Escolha a opção desejada:\n  ')
    elif (voltar == 'N'):
        print('Programa encerrado! \n\n\n')
    else:
        print('Valor inválido. Por favor insira um valor válido.') 

def fecharProg():
    print ("\n" * 2)
    print('Programa encerrado! \n\n\n')

if (resp == '1'):
    listarPontos()
elif (resp == '2'):
    informarLoc()
elif (resp == '3'):
    encontrarPontos()
elif (resp == '4'): 
    buscarLog()
elif (resp == '5'): 
    fecharProg()
else: 
  print('Valor inválido. Por favor insira um valor válido.')