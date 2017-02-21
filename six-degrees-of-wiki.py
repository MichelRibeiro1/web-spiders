from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime, random

random.seed(datetime.datetime.now())
def getLinks(article_url):

	html = urlopen("https://en.wikipedia.org" + article_url)
	bs0bj = BeautifulSoup(html, "lxml")
	return bs0bj.find("div", {"id": "bodyContent"}).findAll("a", {"href": re.compile("^(/wiki/)((?!:).)*$")})

links = getLinks("/wiki/Guido_van_Rossum")
while(len(links) > 0):
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)
