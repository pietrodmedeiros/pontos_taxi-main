
from math import dist, radians, sin, cos, sqrt, asin
from time import sleep

# Fazer leitura do arquivo 'pontos_taxi.csv'
import csv 
csvfile = open('pontos_taxi.csv', encoding="utf8")
array = csv.reader(csvfile, delimiter=';', quotechar=';') # Colocar o texto do csv na variável 'array'
pontosTaxi = []
for row in array:
    pontosTaxi.append(row)

# Texto do menu do progarma
def menu():
    resp =  int(input('''
    ========================================
    |           Pontos de taxi POA         |
    ==================MENU==================  
        Escolha uma das opções abaixo:

        1. Listar todos os pontos de taxi  
        2. Informar localização  
        3. Encontrar pontos próximos
        4. Buscar pontos por logradouro
        5. Fechar o pograma
        
        >: '''))
# Conforme a resposta do usuário, o programa chama a função correta.
    if resp == 1:
        listarPontos()
        voltarMenu()
    elif resp == 2:
        informarLoc()
        voltarMenu()
    elif resp == 3:
        encontrarPontos()
        print(dist)
        voltarMenu()
    elif resp == 4: 
        buscarLog()
        voltarMenu()
    elif resp == 5:
        print(' Encerrando programa...')
        sleep(1)
        print(' \n ... \n')
        sleep(1)
        print(' Programa encerrado!')
        exit()
    else:
        print('Valor inválido. Por favor insira um valor válido.')


# Função para imprimir os campos 'Nome do ponto'; 'Telefone' e 'Endereço'. Cada campo em uma linha.
def listarPontos():   
# Nem todos os pontos cadastrados possuem telefone, então primeiro será verificado em cada linha se a terceira coluna está vazia (coluna telefone).
# Se estiver, será exibida mensagem de telefone não cadastrado no respectivo campo.
    for row in pontosTaxi:
        if (row[3] == ' '):
            print(' Nome do ponto: {} \n  Telefone: Telefone não cadastrado. \n  Endereço: {} {} \n'.format(row[2], row[4], row[5]))
        else:
            print(' Nome do ponto: {} \n  Telefone:{} \n  Endereço: {} {} \n'.format(row[2], row[3], row[4], row[5]))


# Função pergunta a localização do usuário (latitude e longitude) e armazena nas variáveis 'lon1' e 'lat1'.
def informarLoc():
    print(' ')
    global lon1
    global lon2
    lon1 = input('Digite a longitude: \n  ')
    lat1 = input('Digite a latitude \n  ')
    return lat1, lon1


# Função que lista os 3 pontos mais próximos da localização inserida pelo usuário.
# Ainda não está pronta.
# [] Converter os valores de lat e lon para float
# [] Trocar , por .
# [] 
def encontrarPontos():
    dist = []
    for row in array:
        lat2 = row[6]
        lon2 = row[7]
        dist.append(lat2, lon2)
        return dist


# Função que faz o cálculo para dizer a distância do usuário para o ponto de taxi.
def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
 
    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))
    x = R * c
    #return x
    print(x)



# Função que imprime os Pontos de Taxi na rua que o usuário inserir.
def buscarLog():
    log = input('Digite o logradouro ou parte dele: \n  ').upper().strip()
    i = 0
    for row in range(0, len(pontosTaxi)):
        if log in pontosTaxi[row][4]:
            print('Ponto encontrado: ', pontosTaxi[row][2:6])
            i += row
    if i == 0:
        print('Nenhum ponto de taxi encontrado.')

# Função que pergutna se o usuário deseja voltar ao menu.  
def voltarMenu():
        voltar = input('Voltar ao Menu? [S/N] \n').upper()
        if (voltar == 'S'):
            menu()
        elif (voltar == 'N'):
            exit()
        else:
            print('Valor inválido. Por favor insira um valor válido.')



# Após a escolha da opção, o programa define qual a respectiva função que será acionada.
# Após, sempre é chamada a função que pergunta se o usuário deseja voltar ao menu.
menu()