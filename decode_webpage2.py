import requests
from bs4 import BeautifulSoup
def webpage2():
	url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html,"html.parser")
		 
	content = soup.find(class_ = "content drop-cap").find_all("p")
	for string in content:
		print(string.text)
webpage2()

	
	
	
