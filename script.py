from urllib.request import Request, urlopen
import bs4
import sys, os
import requests

if len(sys.argv) < 1:
	print("Error: Enter url as argument in the command line")
url = sys.argv[1]
# opener = urllib.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# response = opener.open(url)
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# html = urllib.request.urlopen(url)
page = requests.get(url).text
soup = bs4.BeautifulSoup(page, features='html.parser')
print(soup)
# imgs = soup.findAll("div", {"id":"divImage"})
# script = soup.findAll('script')
# print(script)
# print(page)
# html = page.text
# print(html)
# html = response.read()
# soup = BeautifulSoup(html, features="html.parser")
# print(soup)
# print(imgs)
# for img in imgs:
	# imgUrl = img.a['href'].split("imgurl=")[1]
	# urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))
for tag in soup.findAll(itemprop="image"): 
    print("inside FOR")
    print(tag['src'])