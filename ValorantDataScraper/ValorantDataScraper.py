from selenium import webdriver   
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup 
import time
  



service = Service(executable_path="C:\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/simeo/AppData/Local/Google/Chrome/User Data")
#options.add_argument("--incognito")
driver = webdriver.Chrome(service = service,options=options)
   
# Navigate to the website   
base_url = "https://google.com"

driver.get(base_url)  
html_source = driver.page_source 

while(True):
      
    soup = BeautifulSoup(html_source, 'html.parser') 
    print(soup.findAll(class_="trn-ign__username"))
    time.sleep(5)

   
# Close the browser to free up resources  
driver.close()