import os
import requests
import time
import pprint
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Parameter
URL_ZILLOW = "https://appbrewery.github.io/Zillow-Clone/"
URL_GOOGLESHEET = "https://docs.google.com/forms/d/e/1FAIpQLSe84LCV7WOEzjbC5NQvI-JaEsqGPHzvLV_sBl33u7DpBv9kJw/viewform?usp=sf_link"

class GetZillowData:
    def __init__(self, URL):
        response = requests.get(URL)
        yc_web_page = response.text
        self.soup = BeautifulSoup(yc_web_page, "html.parser")
        # Check if the file exists
        file_name = 'zillow.txt'
        if not os.path.exists(file_name):
            with open('zillow.txt', 'w') as file:
                file.write(f"{self.soup}")
                print(f"Write html to the {file_name}.")
        else:
            print(f"{file_name} already exists.")
    
    def get_address_list (self):
        address_tags = self.soup.select(selector="address")
        address_list = [address_tag.get_text().strip() for address_tag in address_tags]
        # print(f"address_list = {address_list}")
        # len_address_list = len(address_list)
        # print(f"len_address_list = {len_address_list}") # 44
        return address_list
    
    def get_link_list (self):
        link_tags = self.soup.select(selector=".StyledPropertyCardPhotoBody a")
        link_list = [link_tag.get("href") for link_tag in link_tags]
        # len_link_list = len(link_list)
        # print(f"len_link_list = {len_link_list}") # 44
        return link_list

    def get_price_list (self):
        price_tags = self.soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
        price_list = []
        for price_tag in price_tags:
            price = price_tag.get_text()
            price = price.split("+")[0]
            price = price.replace("/mo","").replace(",","")
            price = price.split("$")[1]
            price = '{:,.0f}'.format(float(price))
            price = "$" + price
            # print(f"price = {price}")
            price_list.append(price)
        # print(f"price_list = {price_list}")
        # len_price_list = len(price_list)
        # print(f"len_price_list = {len_price_list}") # 44
        return price_list


class FillGoogleSheet:
    def __init__(self, URL):
        # Keep Chrome browser open after program finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def fill_the_sheet (self, URL, address, price, link):
        # print(f"method: fill_the_sheet")
        self.driver.get(URL)

        time.sleep(0.3)
        input_address = self.driver.find_element(By.CSS_SELECTOR, value='input[aria-labelledby="i1"]')
        input_address.send_keys(address)

        time.sleep(0.3)
        input_price = self.driver.find_element(By.CSS_SELECTOR, value='input[aria-labelledby="i5"]')
        input_price.send_keys(price)

        time.sleep(0.3)
        input_link = self.driver.find_element(By.CSS_SELECTOR, value='input[aria-labelledby="i9"]')
        input_link.send_keys(link)

        button_sumbit = self.driver.find_element(By.CLASS_NAME, value='l4V7wb')
        button_sumbit.click()
        pass
    
    def driver_quit (self):
        self.driver.quit()
        pass


def main():
    # use beautiful to get the data
    bot_get = GetZillowData(URL_ZILLOW)
    address_list = bot_get.get_address_list()
    price_list = bot_get.get_price_list()
    link_list = bot_get.get_link_list()

    # use selenium to fill the sheet
    bot_fill = FillGoogleSheet(URL_GOOGLESHEET)
    for i in range(0, len(address_list)):
        bot_fill.fill_the_sheet(URL_GOOGLESHEET, address_list[i], price_list[i], link_list[i])
        print(f"Property {i+1} is filled in." )
    bot_fill.driver_quit()
    print(f"All property is filled in." )


if __name__ == "__main__":
    main()





