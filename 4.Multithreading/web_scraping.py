import threading
import requests
from bs4 import BeautifulSoup

urls =[
    'https://www.bing.com/search?q=udemy&form=ANNTH1&refig=69731b20b99c4610bdd73d898b502b10&pc=U531&pqlth=0&assgl=5&sgcn=udemy&qs=HS&sgtpv=HS&smvpcn=0&swbcn=10&sctcn=0&sc=10-0&sp=1&ghc=0&cvid=69731b20b99c4610bdd73d898b502b10&clckatsg=1&hsmssg=0',
    'https://www.instagram.com'
]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Featched {len(soup.text)}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("All URLs have been fetched.")
