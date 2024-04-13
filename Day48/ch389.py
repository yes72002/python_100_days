import time
import pprint
# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://www.python.org/"
driver.get(URL)

# Jim's Code
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]
dict_out = {}
for i in range(1, 6):
    time_sel = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    time_text = time_sel.get_attribute("datetime")
    time_text = time_text.split("T")[0]
    print(time_text)
    name_ele = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    name_text = name_ele.text
    print(name_text)
    dict_temp = {'time':time_text, 'name':name_text, }
    dict_out[i-1] = dict_temp
    

pprint.pprint(dict_out)

# Angela's Code
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close()
driver.quit()
