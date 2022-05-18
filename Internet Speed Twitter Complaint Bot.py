from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by, keys
import time

PROMISED_UP = 20
PROMISED_DOWN = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        options = webdriver.ChromeOptions()
        options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.driver = webdriver.Chrome(options=options, service=Service("../venv/chromedriver.exe"))
        self.driver.maximize_window()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        self.driver.find_element(by.By.CSS_SELECTOR, value=".start-button a").click()
        time.sleep(60)

        self.down = self.driver.find_element(by.By.XPATH,
                                             "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div["
                                             "3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.up = self.driver.find_element(by.By.XPATH,
                                           "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div["
                                           "3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        self.driver.find_element(by.By.XPATH,
                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div['
                                       '3]/div[5]/a').click()
        time.sleep(5)
        self.driver.find_element(by.By.CLASS_NAME, value='r-fdjqy7').send_keys(f"________{keys.Keys.ENTER}")
        time.sleep(5)
        self.driver.find_element(by.By.CLASS_NAME, value='r-fdjqy7').send_keys(f"________{keys.Keys.ENTER}")
        time.sleep(5)
        self.driver.find_element(by.By.XPATH,
                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div['
                                       '2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div['
                                       '1]/div/div/div/div[2]/div/div/div/div').send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}"
            f"down/{PROMISED_UP}up?")
        time.sleep(5)
        self.driver.find_element(by.By.XPATH,
                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div['
                                       '2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]').click()
        time.sleep(10)
        self.driver.quit()


InternetSpeedTwitterBot().get_internet_speed()
InternetSpeedTwitterBot().tweet_at_provider()
