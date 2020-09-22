import requests
from bs4 import BeautifulSoup



page = requests.get('http://www.theartgardenrohingya.com/')

bSoup = BeautifulSoup(page.content, 'html.parser')
linkList = bSoup.find_all('a')

for link in linkList:
    if 'href' in link.attrs:
        file1 = open("linkDocs.txt","w") 
        l= (str(link.attrs['href']+ "\n"))
        #print(l)
        file1.writelines(l)
print('Done!')
        
        

file1.close()
