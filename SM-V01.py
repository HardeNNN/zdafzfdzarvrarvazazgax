from bs4 import BeautifulSoup
import urllib.request
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


url = input('What site are you working on today, sir?\n\n ')
opener = AppURLopener()
html_page = opener.open(url)
soup = BeautifulSoup(html_page, "lxml")
for link in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
     print ('\n',link.get('href'),'\n',file=open("magnets.txt", "a"))
