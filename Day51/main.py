import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from secret_key import TWITTER_EMAIL, TWITTER_PASSWORD
# Parameter
# TWITTER_EMAIL = "xxxxxxxx"
# TWITTER_PASSWORD = "xxxxxxxx"

class InternetSpeedTwitterBot:
    def __init__(self, URL):
        # Keep Chrome browser open after program finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(options=chrome_options)

        # self.driver = driver.get(URL)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed (self):
        print(f"method: get_internet_speed")
        # Copy from Angela's solution
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        speed = 0
        return speed
    
    def tweet_at_provider (self):
        print(f"method: tweet_at_provider")
        done = True
        print(f"Tweet at provider succeed")
        # XML data successfully written to Excel file:
        return done

# URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
# URL = "https://twitter.com/"
URL = "https://twitter.com/i/flow/login"
# driver.get(URL)

# Speedtest
# URL_speedtest = "https://www.speedtest.net/"
# driver.get(URL_speedtest)
# time.sleep(5)
# go = driver.find_element(By.CLASS_NAME, value="start-text")
# go.click()

bot = InternetSpeedTwitterBot(URL)
bot.get_internet_speed()
bot.tweet_at_provider()


exit()


