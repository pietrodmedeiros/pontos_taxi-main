menu = ('========================================\n|           Pontos de taxi POA         |\n==================MENU================== \n  1. Listar todos os pontos de taxi \n  2. Informar localização \n  3. Encontrar pontos próximos \n  4. Buscar pontos por logaradouro \n  5. Fechar o pograma')

print(menu)

resp = input('Escolha a opção desejada:\n  ')

def listarPontos():
    print('Lista com os pontos de taxi de POA')
    voltar = input('Voltar ao Menu? [S/N] \n')
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
    print(' ')
    log = input('Digite o logradouro ou parte dele: \n  '),
    print(log)
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