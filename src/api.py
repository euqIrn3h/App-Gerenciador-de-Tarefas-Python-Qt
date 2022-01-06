import requests
import re

def Clima():
    '''with open("keys.txt",'r') as arquivo:
        key = arquivo.read()

    padrao = re.compile('#key-hg-weather')
    key0 = padrao.search(key)
    padrao = re.compile('#')
    key1 = padrao.search(key[key0.span()[1]:])
    key = key[key0.span()[1]:]
    key = key[:key1.span()[0]]''' #caso voce quiera mascarar a key da api em um arquivo gitgnore

    key = '181c7dc7'

    r = requests.get(f"https://api.hgbrasil.com/geoip?key={key}&address=remote&precision=false")
    r = requests.get(f"https://api.hgbrasil.com/weather?woeid={r.json()['results']['woeid']}")
    # r.json()['results']['woeid'] Codigo da cidade

    return r.json()['results']['city'],r.json()['results']['temp'],r.json()['results']['description'],r.json()['results']['forecast']

