from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

#Create an instance of chrome
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(options=option)
browser.get("https://readcomiconline.to/Comic/Constantine/Issue-6?id=1466&readType=1")

# Wait 7 seconds for page to load
timeout = 7
try:
    WebDriverWait(browser, timeout)
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

search_field = browser.findElement(By.id("divImage"))
print(search_field)    