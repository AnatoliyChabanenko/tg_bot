import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://nibulon.com/'
URL = 'https://nibulon.com/data/zakupivlya-silgospprodukcii/zakupivelni-cini.html'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    'accept': '*/*'}



def get_htms(url , params= None):
    r = requests.get(url, headers = HEADERS, params=params)
    return r



def get_content(html):
    soup = BeautifulSoup(html.text , 'html.parser')
    items = soup.find_all('strong' , limit=7)
    return  items




def main():
    z = []
    d = get_htms(URL)
    contetnt = get_content(d)
    for i in contetnt:
        z.append(list(i))
    return z

def json_damp(data):
    with open('data.json', 'w') as f:
        json.dump(data , f)


if __name__ == '__main__':
    d = dict(enumerate(main()))
    json_damp(d)





