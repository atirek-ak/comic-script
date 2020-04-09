import urllib.request
from bs4 import BeautifulSoup
import sys, os

if len(sys.argv) < 1:
	print("Error: Enter url as argument in the command line")
url = sys.argv[1]
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, features="html.parser")
for img in imgs:
        imgUrl = img.a['href'].split("imgurl=")[1]
        urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))
# imgs_div = soup.findAll("div", {"id":"divImage"})
