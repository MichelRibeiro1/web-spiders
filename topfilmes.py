from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#Informações obtidas através do site adorocinema.com

def filmes_em_cartaz(top_filmes):
	html = urlopen("http://www.adorocinema.com/filmes/numero-cinemas/")
	bsobj = BeautifulSoup(html, "lxml")  
	filmes = bsobj.findAll("a", {"class": "no_underline","href": re.compile("^/filmes/filme(\-)([0-9])+/$")})
	for filme in range(1,int(top_filmes)+1):
		print(str(filme) +"-" +filmes[filme].get_text().strip())

top = input('Qual o top de filmes em cartaz deseja visualizar? ')
filmes_em_cartaz(top)

