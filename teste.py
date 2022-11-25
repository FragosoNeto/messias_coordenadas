import requests
import json

def coordenadas(cidade):
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
    print(objetos)



coordenadas('londres')
