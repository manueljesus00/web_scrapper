from bs4 import BeautifulSoup
import requests
import urllib
url = "https://www.directoalpaladar.com/categoria/postres/record/20"
webpage=str(urllib.request.urlopen(url).read())
counter = 0
r = requests.get(url)
code_status = r.status_code

if code_status == 200:
    html = BeautifulSoup(webpage, features='html.parser')
    entradas = html.find_all('article')
    for item in entradas:
        counter += 1
        titulo = item.find('h2', {'class':'abstract-title'}).getText()
        link = item.find('a').get('href')

        print("Id........: %d" % counter)
        print("Titulo....: " + cor_titulo)
        print("Link......: " + link)
        print("______________________________________")
else:
    print ("Error en la página")