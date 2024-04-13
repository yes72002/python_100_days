import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)


article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count_text = article_count.text
# print(article_count_text)
# article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)
# search.send_keys()




time.sleep(3)
driver.quit()
