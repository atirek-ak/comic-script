from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import sys, os

def parse_url(url):
	url = url + '&readType=1'
	return url

def extract_source_code(url):
	#Create an instance of chrome
	options = webdriver.ChromeOptions();
	options.add_argument('headless'); #to not open a browser window
	options.add_argument('--load-images=no');
	browser = webdriver.Chrome(options=options)
	browser.get(url)

	# Wait 7 seconds for page to load
	timeout = 7
	try:
    	WebDriverWait(browser, timeout)
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

def main():
	#accept link as argument
	if len(sys.argv) < 2:
		print("Enter url as argument in the command line")
		sys.exit()
	url = parse_url(sys.argv[1])
	extract_source_code(url) #stores source code of url in 'source.txt'
	

main()