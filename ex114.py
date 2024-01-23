import urllib.request
try:
    url = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'O site do pudim não está acessivel.')
else:
    print('O site do pudim está acessivel normal!')


# FUNÇÃO DE VALIDAÇÃO DE SITE
"""import requests
def verificar_acessibilidade(url):
    try:
        responde = requests.get(url)
        if responde.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False


# URL do site "http://www.pudim.com.br"
url_pudim = "http://www.pudim.com.br"


# Testar a acessibilidade do site
if verificar_acessibilidade(url_pudim):
    print(f'O site {url_pudim} está acessivel.')
else:
    print(f'O site {url_pudim} não está acessivel.')
    #print(site.read())"""
