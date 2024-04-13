import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from secret_key import LINKEDIN_USERNAME, LINKEDIN_PASSWORD

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(URL)

loggin = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
loggin.click()

username = driver.find_element(By.ID, value="username")
username.send_keys(LINKEDIN_USERNAME)
password = driver.find_element(By.ID, value="password")
password.send_keys(LINKEDIN_PASSWORD)
button = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
button.click()

# easyapply = driver.find_element(By.CLASS_NAME, value="artdeco-button__text")
# ID not work, it would change
# easyapply = driver.find_element(By.CSS_SELECTOR, value="button[class='jobs-apply-button'] span")
easyapply = driver.find_element(By.CLASS_NAME, value="jobs-apply-button")
easyapply.click()
time.sleep(3)

phonenumber = driver.find_element(By.CLASS_NAME, value="artdeco-text-input--input")
phonenumber.send_keys("0975852779")

# span 不能click，要找button
# phonenumber_next = driver.find_element(By.CLASS_NAME, value="artdeco-button__text")
phonenumber_next = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
phonenumber_next.click()

phonenumber_next.click()

# time.sleep(3)
# driver.quit()
