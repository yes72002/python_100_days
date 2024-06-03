import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

cookie = driver.find_element(By.ID, value="cookie")
cookie.click()
for i in range(100):
    cookie.click()


money = driver.find_element(By.ID, value="money")
money_num = int(money.text)
print(f"money_num = {money_num}")


count = 0
game = True
while game == True:
    buy_cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b")
    buy_curosr_num = int(buy_cursor.text.split(" ")[-1].replace(",",""))
    print(f"buy_curosr_num = {buy_curosr_num}")

    buy_grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
    buy_grandma_num = int(buy_grandma.text.split(" ")[-1].replace(",",""))
    print(f"buy_grandma_num = {buy_grandma_num}")

    buy_factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b")
    buy_factory_num = int(buy_factory.text.split(" ")[-1].replace(",",""))
    print(f"buy_factory_num = {buy_factory_num}")

    buy_mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine b")
    buy_mine_num = int(buy_mine.text.split(" ")[-1].replace(",",""))
    print(f"buy_mine_num = {buy_mine_num}")

    buy_shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b")
    buy_shipment_num = int(buy_shipment.text.split(" ")[-1].replace(",",""))
    print(f"buy_shipment_num = {buy_shipment_num}")

    # buy_alchemy = driver.find_element(By.CSS_SELECTOR, value="#buyAlchemy lab b")
    # buy_alchemy_num = int(buy_alchemy.text.split(" ")[-1].replace(",",""))
    # print(f"buy_alchemy_num = {buy_alchemy_num}")

    buy_portal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")
    buy_portal_num = int(buy_portal.text.split(" ")[-1].replace(",",""))
    print(f"buy_portal_num = {buy_portal_num}")

    # buy_time_machine = driver.find_element(By.CSS_SELECTOR, value="#buyTime machine b")
    # buy_time_machine_num = int(buy_time_machine.text.split(" ")[-1].replace(",",""))
    # print(f"buy_time_machine_num = {buy_time_machine_num}")


    money = driver.find_element(By.ID, value="money")
    money_num = int(money.text.replace(",",""))
    print(f"money_num = {money_num}")

    if money_num > buy_portal_num:
        buy_portal.click()
    elif money_num > buy_shipment_num:
        buy_shipment.click()
    elif money_num > buy_mine_num:
        buy_mine.click()
    elif money_num > buy_factory_num:
        buy_factory.click()
    elif money_num > buy_grandma_num:
        buy_grandma.click()
    elif money_num > buy_curosr_num:
        buy_cursor.click()
    else:
        for i in range(100):
            cookie.click()
    
    # determine every one second
    time.sleep(1)
    print(count)
    count += 1
    # If time over 5 mins, exit the while loop
    if count >= 5*60:
        score = driver.find_element(By.ID, value="cps")
        # buy_portal_num = int(score.text)
        print(f"{score.text}")
        break



# time.sleep(3)
driver.quit()
