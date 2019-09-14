from bs4 import BeautifulSoup
import requests

url = "https://www.directoalpaladar.com/categoria/postres/record/20"
counter = 0
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
articulos = soup.find_all('h2', {'class':'abstract-title'})

if len(articulos) > 0:
    for articulo in articulos:
        counter += 1
        link = articulo.find('a').get('href')
        titulo = articulo.get_text()
        print("Id........: %d" % counter)
        print("Titulo....: " + titulo)
        print("Link......: " + link)
        print("______________________________________")
else:
    print ("Error en la página")