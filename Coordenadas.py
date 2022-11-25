import requests
import json

def coordenadas(lat,log):
    API_KEY = 'c0a6c9f21eb7b95c3d7227ce9d0e6d0d'
    #LAT = ["38.7167","40.4165","43.2128","48.8534","51.5085"]
    #LOG = ["-9.1333","-3.7026","-75.4557","2.3488","-0.1257"]
    url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={log}&appid={API_KEY}")
    resposta   = requests.request("GET", url)
    objetos    = json.loads(resposta.text)
    pais = objetos["sys"]["country"]
    city = objetos["name"]
    long = objetos["coord"] ["lon"]
    lat = objetos["coord"] ["lat"]
    dados = 'dados.txt'
    with open(dados, 'a', encoding='utf-8') as dados:
        dados.write(f"{pais}, {city}, {lat},{long}\n")
        print(f" {pais}, {city}, {lat},{long}")

def coordenadas1(cidade):
    API_KEY = 'c0a6c9f21eb7b95c3d7227ce9d0e6d0d'
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric")
    resposta   = requests.request("GET", url)
    objetos    = json.loads(resposta.text)
    pais = objetos["sys"]["country"]
    city = objetos["name"]
    long = objetos["coord"] ["lon"]
    lat = objetos["coord"] ["lat"]
    dados = 'dados.txt'
    with open(dados, 'a', encoding='utf-8') as dados:
        dados.write(f"{pais}, {city}, {lat},{long}\n")
        print(f" {pais}, {city}, {lat},{long}")

cidades=[]
geral=[]
while True:
    print('-' * 30)
    print('             MENU            ')
    print('-' * 30)
    print('1-Cadastrar cidades.')
    print('2-Cidades Cadastradas.')
    print('3-Informações do clima.')
    print('4-Consulta por nome da cidade.')
    print('5-Sair.')
    print('-' * 30)

    try:
        op=int(input('Escolha uma das operações:'))
        print('-' * 30)
    except (ValueError, TypeError):
        print("Por favor, insira somente números")

    if op==1:
        cidade=str(input('Informe o nome da cidade: ')).strip().upper()
        lat=str(input('Informe a latitude: '))
        log=str(input(('Informe a longitude: ')))
        cidades=[cidade,lat,log]
        geral.append(cidades)

    elif op==2:
        for i in enumerate(geral):
            print(i)

    elif op==3:
        for i in enumerate(geral):
            print(i)
        try:
            op1=int(input('Informe o número da cidade cadastrada:'))
            lat = geral[op1][1]
            log = geral[op1][2]
            coordenadas(lat, log)
        except (ValueError, TypeError):
            print("Por favor, insira somente números")

    elif op==4:
        cidade=str(input('Informe o nome da cidade desejada:')).strip().lower()
        coordenadas1(cidade)

    elif op==5:
        print('Fim do programa')
        break

    else:
        print('Informe o número referente a uma das opções.')
