from bs4 import BeautifulSoup
from os import listdir
import plotly.graph_objs as go

folder = 'pages'
min_price = 2000
max_price = 20000
step = 1000
count = 89

def getHtml(path):
    return open(path).read()
    
def getPrices(path):
    prices = []
    html = getHtml(path)
    soup = BeautifulSoup(html, 'html.parser')
    prices = [int(p['content']) for p in soup.find_all("meta",  itemprop="price")[:count] if p['content'].isdigit() and int(p['content']) <= max_price and int(p['content']) >= min_price]
    # prices = [p - p % step for p in prices]
    return prices

def getAverage(prices):
    return sum(prices) / len(prices)

def getHistogram(prices):
    xbins = go.histogram.XBins(size=step)
    fig = go.Figure(data=[go.Histogram(x=prices, xbins=xbins)])
    fig.show()

def main():
    pages = [folder + '/' + p for p in listdir(folder) if p.split('.')[1] == 'html']
    prices = []
    for p in pages:
        prices += getPrices(p)
    print(f'AVERAGE PRICE = {getAverage(prices)}')
    getHistogram(prices)

if __name__ == '__main__':
    main()