from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import sys, os, requests
from PIL import Image #convert image to pdf
import shutil
import time

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

def extract_source_code(url, file):
	browser.get(url)

	# Wait 60 seonds for page to load
	timeout = 60
	try:
		element = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, "containerRoot")))
	except TimeoutException:
		print("Timed out waiting for page to load")
		browser.quit()

	#store source code in a .txt file
	source_Code = browser.page_source
	soure_file = open(file,'w')
	soure_file.write(source_Code)
	soure_file.flush()
	soure_file.close()


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
	pdf_directory = os.path.join(cur_dir, "Comics", comic)
	if not os.path.exists(final_directory):
		os.makedirs(final_directory)
	return final_directory, pdf_directory

def delete_directory(comic, issue):
	cur_dir = os.getcwd()
	final_directory = os.path.join(cur_dir, "Comics", comic, issue)
	os.rmdir(final_directory)

def download_comic(path, links, issue, comic):
	print("Downloading " + comic + " " + issue)
	# print(path)
	count = 1
	session = requests.session()
	for image in links:
		r = session.get(image)
		with open(path + "/" + str('%03d' % count) + ".jpg", 'wb') as f:
			f.write(r.content)
		print("Downloading " + '%03d' % count)
		# if count>=10 and count%10 == 1:
			# time.sleep(1)
		count += 1
	print("Download complete.")		

def convert_to_pdf(comic, issue):
	pdf = []
	files = []
	# cur_dir = os.getcwd()
	# final_dir = os.path.join(cur_dir, "Comics", comic) #to store pdf
	# jpg_directory = os.path.join(cur_dir, "Comics", comic, issue) #where images are stored
	jpg_directory, final_dir = create_directory(comic, issue)
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

def single_comic(link):
	url, comic, issue = parse_url(link)
	path, pdf_directory = create_directory(comic, issue)
	name = comic + "-" + issue + ".pdf" #in case comic exists
	# print(pdf_directory + "/" + name)
	if os.path.isfile(pdf_directory + "/" + name):
		delete_directory(comic, issue)
		print(name + " already exists")
		return
	extract_source_code(url, "source.txt") #stores source code of url in 'source.txt'
	links = extract_image_links() #stores links of all images in links list
	links = refine_links(links)
	os.remove("source.txt")
	download_comic(path, links, issue, comic)
	convert_to_pdf(comic, issue)
	print('The comic is at: ' + pdf_directory)
	shutil.rmtree(path)

def download_issue(comic):
	extract_source_code(sys.argv[1], "issue.txt")
	# comic = 
	links = []
	with open("issue.txt", "r") as a_file:
		for line in a_file:	
			if comic in line and "?id" in line:
					links.append(line.split('"')[1])
	# links.reverse()
	num=0				
	for link in links:
		# num+=1
		# if(num<34):
			# continue
		print()
		single_comic("https://readcomiconline.to/"+link)
		# time.sleep(1)
	if os.path.isfile("issue.txt"):
		os.remove("issue.txt")	


def	check_url():
	#accept link as argument
	if len(sys.argv) < 2:
		print("Enter url as argument in the command line")
		sys.exit()
	link = 	sys.argv[1].split('/')
	if len(link) == link.index('Comic') + 2 or "id" not in link[link.index('Comic') + 2]:
		download_issue("Comic/" + link[link.index('Comic') + 1])
	else:
		single_comic(sys.argv[1])

print("Firing up Chrome...")
#Create an instance of chrome
options = webdriver.ChromeOptions();
# options.add_argument('headless'); #to not open a browser window
options.add_argument('--load-images=no'); #to lower loading time
browser = webdriver.Chrome(options=options)
check_url()
browser.quit()