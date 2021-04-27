from bs4 import BeautifulSoup
from os import listdir

folder = 'pages'

def getHtml(path):
    return open(path).read()
    
def getPrices(path):
    prices = []
    html = getHtml(path)
    soup = BeautifulSoup(html, 'html.parser')
    prices = [int(p['content']) for p in soup.find_all("meta",  itemprop="price") if p['content'].isdigit()]
    return prices

def main():
    pages = [folder + '/' + p for p in listdir(folder) if p.split('.')[1] == 'html']
    prices = []
    for p in pages:
        prices += getPrices(p)
    print(prices)

if __name__ == '__main__':
    main()