import requests

def get_article(url):
    html=requests.get(url)
    return html



