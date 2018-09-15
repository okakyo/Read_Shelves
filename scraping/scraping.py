import requests
from bs4 import BeautifulSoup
def get_article(url):
    html=requests.get(url)
    return BeautifulSoup(html.text,'lxml').prettify()

if __name__ == '__main__':
    print(get_article('https://qiita.com/juniskw/items/7fa72f91e3dc899a80ae'))




