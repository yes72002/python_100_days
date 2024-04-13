import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

fName = driver.find_element(By.NAME, value="fName")
fName.send_keys("Yuan Jin")
lName = driver.find_element(By.NAME, value="lName")
lName.send_keys("Li")
email = driver.find_element(By.NAME, value="email")
email.send_keys("yes72002@gmail.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()


time.sleep(3)
driver.quit()
