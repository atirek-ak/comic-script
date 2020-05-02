from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import sys, os, requests
from PIL import Image #convert image to pdf

# from datetime import datetime #for testing purpose

def parse_url(url):
	if '&readType=1' in url:
		url = url + '&readType=1'
	link = 	url.split('/')
	comic = link[link.index('Comic') + 1]
	issue = link[link.index('Comic') + 2]
	issue = issue.split('?')[0]
	# print(comic)
	# print(issue)
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

def create_directory(comic, issue):
	cur_dir = os.getcwd()
	final_directory = os.path.join(cur_dir, "Comics", comic, issue)
	if not os.path.exists(final_directory):
		os.makedirs(final_directory)
	return final_directory	

def download_comic(path, links):
	# print(path)
	count = 1
	for image in links:
			r = requests.get(image)
			with open(path + "/" + str('%03d' % count) + ".jpg", 'wb') as f:
				f.write(r.content)
			print("Downloading " + '%03d' % count + ".jpg")
			count += 1

def convert_to_pdf(comic, issue):
	pdf = []
	files = []
	cur_dir = os.getcwd()
	final_dir = os.path.join(cur_dir, "Comics", comic) #to store pdf
	jpg_directory = os.path.join(cur_dir, "Comics", comic, issue) #where images are stored
	for filename in os.listdir(jpg_directory):
		if filename.endswith(".jpg"):
			files.append(filename)
	files.sort(key=str) #sort files 
	image1 = Image.open(jpg_directory + "/" + files[0])
	im1 = image1.convert('RGB')
	for filename in files[1:]:	
		image = Image.open(jpg_directory + "/" + filename)
		im = image.convert('RGB')
		pdf.append(im)
	name = comic + "-" + issue + ".pdf" #name of pdf
	im1.save(final_dir + "/" + name, save_all=True, append_images=pdf)	
	print("Comic converted to pdf")

def main():
	#accept link as argument
	if len(sys.argv) < 2:
		print("Enter url as argument in the command line")
		sys.exit()
	pdf = input('Convert comic from images to .pdf file(y/n): ')	
	url, comic, issue = parse_url(sys.argv[1])
	extract_source_code(url) #stores source code of url in 'source.txt'
	links = extract_image_links() #stores links of all images in links list
	links = refine_links(links)
	os.remove("source.txt")
	path = create_directory(comic, issue)
	download_comic(path, links)
	if pdf[0] in ['y', 'Y']:
		convert_to_pdf(comic, issue)
main()