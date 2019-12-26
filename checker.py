from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

args = sys.argv
if len(args) != 3:
    print("Usage: python file.py username password")
    sys.exit()
else:
    try:
        username = args[1]
        password = args[2]
    except:
        sys.exit()

driver = webdriver.Chrome("drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://mysu.sabanciuniv.edu/up/internet_usage")
time.sleep(1)
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("submit").click();

#driver.get("https://mysu.sabanciuniv.edu/up/internet_usage")
try:
    usage = driver.find_element_by_class_name("td_data").text
    if(len(usage) < 1):
        print("No usage information given.")
        driver.quit()
        sys.exit()
    else:
        left = str(8.0 - float(usage[:-3]))
        if float(left) <= 0:
            print("You have exceeded your limit. Your current usage is" + usage)
        else:
            print("You have used: " + usage + ". You can still use " + left + " GB.")
        driver.quit()
except:
    print("No usage information given.")
    driver.quit()
    sys.exit()
    
