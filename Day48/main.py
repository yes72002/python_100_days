import time
# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

########################
# Amazon
########################
# URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# driver.get(URL)

# price_dollor = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollor.text}.{price_cents.text}")

# # driver.close() # close one tag
# driver.quit() # close all browser, quit entire program

########################
# PChome
########################
# URL = "https://24h.pchome.com.tw/prod/DYAPGD-A900F37FC"
# driver.get(URL)

# price_cents = driver.find_element(By.CLASS_NAME, value="o-prodPrice__price")
# print(f"The price is {price_cents.text}")

# search_bar = driver.find_element(By.CLASS_NAME, value="c-search__input")
# print(search_bar) # return in selenium element
# print(search_bar.tag_name) # input
# print(search_bar.get_attribute("autocomplete")) # off

# button = driver.find_element(By.CLASS_NAME, value="o-iconFonts")
# print(button.tag_name) # i
# print(button.size) # {'height': 14, 'width': 14}

# # driver.close()
# driver.quit()

########################
# Python document
########################
URL = "https://www.python.org/"
driver.get(URL)

# by NAME
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar) # return in selenium element
print(search_bar.tag_name) # input
print(search_bar.get_attribute("placeholder")) # Search

# by ID
button = driver.find_element(By.ID, value="submit")
print(button.tag_name) # button
print(button.size) # {'height': 39, 'width': 46}

# by css selector
# docs.python.org link
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text) # docs.python.org

# by XPath
# Submit Website Bug
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text) # Submit Website Bug



# driver.close()
driver.quit()
