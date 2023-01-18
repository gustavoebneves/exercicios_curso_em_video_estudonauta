# http://www.pudim.com.br
import urllib.request
site = str(input('Qual site você quer checar a conexão? '))
try:
    urllib.request.urlopen(site)
except:
    print('Não consegui acessar o site :(')
else:
    print('Consegui!')

