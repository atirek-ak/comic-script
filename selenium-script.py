from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import sys, os
from datetime import datetime #for testing purpose

def parse_url(url):
	if '&readType=1' in url:
		url = url + '&readType=1'
	link = 	url.split('/')
	comic = link[link.index('Comic') + 1]
	issue = link[link.index('Comic') + 2]
	issue = issue.split('?')[0]
	print(comic)
	print(issue)
	return url, comic, issue

def extract_source_code(url):
	#Create an instance of chrome
	options = webdriver.ChromeOptions();
	# options.add_argument('headless'); #to not open a browser window
	options.add_argument('--load-images=no'); #to lower loading time
	browser = webdriver.Chrome(options=options)
	browser.get(url)

	# Wait 7 seonds for page to load
	timeout = 7
	try:
		element = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, "containerRoot")))
	except TimeoutException:
		print("Timed out waiting for page to load")
		browser.quit()

	#store source code in a .txt file
	source_Code = browser.page_source
	soure_file = open('source.txt','w')
	soure_file.write(source_Code)
	soure_file.flush()
	soure_file.close()
	browser.quit()

def extract_image_links():
	links = []
	with open("source.txt", "r") as a_file:
		for line in a_file:	
			if 'blogspot' in line:
				if 'src' in line:
					pass
				else:
					links.append(line.split('"')[1])	
	return links

def refine_links(links):
	#for high quality
	for link in links:
		if '=s1600' in link:
			link.replace("=s1600", "=s0")
	return links		

def download_comic(comic, issue, links):
	path = os.getcwd()
	print(path) 
	# os.mkdir("./" + path)
	# print("done")	

def main():
	#accept link as argument
	if len(sys.argv) < 2:
		print("Enter url as argument in the command line")
		sys.exit()
	url, comic, issue = parse_url(sys.argv[1])
	start = datetime.now()
	extract_source_code(url) #stores source code of url in 'source.txt'
	links = extract_image_links() #stores links of all images in links list
	# print(links)
	finish = datetime.now() - start
	print(finish)
	links = refine_links(links)
	download_comic(comic, issue, links)

main()