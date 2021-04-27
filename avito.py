from bs4 import BeautifulSoup
from os import listdir

folder = 'pages'

def main():
    pages = [folder + '/' + p for p in listdir(folder) if p.split('.')[1] == 'html']
    print(pages)

if __name__ == '__main__':
    main()