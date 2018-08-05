# This is a script that extracts magnet links with more than 0 seeds from a
# specified link, Special thanks to Andrej Kesely!
from bs4 import BeautifulSoup
import requests
import urllib.request
from pprint import pprint


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


url = input('What site you working on today, sir?\n-> ')

opener = AppURLopener()
html_page = opener.open(url)
soup = BeautifulSoup(requests.get(url).text, 'lxml')
tds = soup.select('#searchResult td.vertTh ~ td')
links = [name.select_one('a[href^=magnet]')['href'] for name, seeders, leechers in zip(tds[0::3], tds[1::3], tds[2::3]) if seeders.text.strip() != '0']
with open('magnetswseeds.txt', 'wt') as out:
    pprint(links, width=120, stream=out)
print(*links, sep="\n", file=open("magnetsnolist.txt", "w"))
