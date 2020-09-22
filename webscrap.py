import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.theartgardenrohingya.com/')

bSoup = BeautifulSoup(page.content, 'html.parser')
linkList = bSoup.find_all('a')

with open("linkDocs.txt", "a") as file1:
    for link in linkList:
        if 'href' in link.attrs:
            file1.writelines(str(link.attrs['href']+ "\n"))
            
            
print('Done!')
file1.close()
        

