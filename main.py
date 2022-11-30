import os
import dotenv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


dotenv.load_dotenv(".env")
PASSWORD = os.getenv("LINKEDIN_PASS")
EMAIL = os.getenv("EMAIL")

chrome_driver_path = Service("/home/jacob/Development/chromedriver_linux64/chromedriver")
chrome_driver = webdriver.Chrome(service=chrome_driver_path)
chrome_driver.maximize_window()
chrome_driver.get("https://www.linkedin.com/")

chrome_driver.find_element(By.XPATH, "/html/body/nav/div/a[2]").click()
time.sleep(2)
chrome_driver.find_element(By.XPATH, """//*[@id="username"]""").send_keys(EMAIL)
chrome_driver.find_element(By.XPATH, """//*[@id="password"]""").send_keys(PASSWORD)
chrome_driver.find_element(By.XPATH, """//*[@id="organic-div"]/form/div[3]/button""").click()





