import requests
from bs4 import BeautifulSoup
def decode():
	url = "https://www.nytimes.com"
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html, "html.parser")
	
	content = soup.find(id = "main").find(class_= "span-ab-layout")
	for link in content("a"):
		print(link.get("href"))

decode()

		
	 
