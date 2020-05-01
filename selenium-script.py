from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import sys, os

def parseUrl(url):
	url = url + '&readType=1'
	return url

def main():
	#accept link as argument
	if len(sys.argv) < 2:
		print("Enter url as argument in the command line")
		sys.exit()
	url = sys.argv[1]
	url = parseUrl(url)

	#Create an instance of chrome
	# driver = webdriver.PhantomJS(service_args=['--load-images=no'])
	options = webdriver.ChromeOptions();
	options.add_argument('headless');
	options.add_argument('--load-images=no');
	browser = webdriver.Chrome(options=options)

	# option.add_argument(" — incognito")
	# browser = webdriver.Chrome(options=driver)
	# browser = webdriver.PhantomJS(service_args=['--load-images=no'])
	browser.get("https://readcomiconline.to/Comic/Constantine/Issue-6?id=1466&readType=1")
	# Wait 7 seconds for page to load
	timeout = 7
	# try:
    	# WebDriverWait(browser, timeout).until(
				# EC.presence_of_element_located((By.ID, "divImage")))
	# except TimeoutException:
    	# print("Timed out waiting for page to load")
    	# browser.quit()

	source_Code = browser.page_source
	soure_file = open('source.txt','w')
	soure_file.write(source_Code)
	soure_file.flush()
	soure_file.close()
	browser.quit()
	# search_field = browser.findElement(By.ID, "divImage")
	# print(search_field)    

main()