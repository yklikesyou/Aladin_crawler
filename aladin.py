import requests
from bs4 import BeautifulSoup


def get_books_info():
    subjects =[]

    for n in range (3) :
        req = requests.get('https://www.aladin.co.kr/UsedStore/wNewUsedBook.aspx?offcode=Sinsa&ViewRowsCount=25&SortOrder=2&page='+ str(n) +'&PriceFilterMin=0&PriceFilterMax=0')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        divs = soup.find_all("a", "bo_l") 

    for div in divs:
        links = div.findAll('b')

        for link in links:
          subject = link.text
          subjects.append(subject)
    return subjects

Books = get_books_info()
print(Books)

