from bs4 import BeautifulSoup
import requests
import urllib
url = "https://www.directoalpaladar.com/categoria/postres/record/20"
webpage=str(urllib.request.urlopen(url).read())
soup = BeautifulSoup(webpage)
counter = 0
r = requests.get(url)
code_status = r.status_code
if code_status == 200:
    html = BeautifulSoup(webpage, 'html.parser')
    entradas = html.find_all('article', {'class': 'recent-abstract abstract-title'})
    entradas2 = html.find_all('article', {'class': 'recent-abstract abstract-title m-featured'})

    for item in entradas2:
        entradas.append(item)
    for item in entradas:
        cont += 1
        titulo = item.find('h2', {'class':'abstract-title'}).getText()
        link = item.find('a').get('href')

        print("Id........: %d" % cont)
        print("Titulo....: " + titulo)
        print("Link......: " + link)
        print("______________________________________")
else:
    print ("Error "+code_status+" en la página")