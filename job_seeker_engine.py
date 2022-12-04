import os
import dotenv
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

dotenv.load_dotenv(".env")


class JobSeekerEngine:
    def __init__(self):
        self.PASSWORD = os.getenv("LINKEDIN_PASS")
        self.EMAIL = os.getenv("EMAIL")
        self.PHONE_NUMBER = os.getenv("PHONE_NUMBER")
        self.chrome_driver_path = Service("/home/jacob/Development/chromedriver_linux64/chromedriver")
        self.chrome_driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.chrome_driver.minimize_window()
        self.job_type = ""
        self.experience_level = int
        self.wait = WebDriverWait(self.chrome_driver, 7)

    def get_user_input(self):
        """Asks user a Job Type and Experience level"""
        checking_job_type = True
        while checking_job_type:
            try:
                self.job_type = str(input("What type of job are you interested in?\n"))
            except ValueError:
                print("Please enter words only.")
                continue
            else:
                checking_job_type = False
        checking_experience_level = True
        while checking_experience_level:
            try:
                self.experience_level = int(input(f"Please choose an experience level: \n1. Internship\n"
                                                  f"2. Entry level\n"
                                                  f"3. Associate\n"
                                                  f"4. Mid-Senior level\n"))
                if self.experience_level not in range(1, 5):
                    print("Please enter a valid experience level 1-4.")
                    continue
            except ValueError:
                print("please enter numbers only.")
                continue
            else:
                checking_experience_level = False
        return self.job_type, self.experience_level

    def login_linkedin(self):
        """Logging in LinkedIn"""
        self.chrome_driver.get("https://www.linkedin.com/")
        self.chrome_driver.maximize_window()
        self.chrome_driver.find_element(By.XPATH, "/html/body/nav/div/a[2]").click()
        time.sleep(2)
        self.chrome_driver.find_element(By.XPATH, """//*[@id="username"]""").send_keys(self.EMAIL)
        self.chrome_driver.find_element(By.XPATH, """//*[@id="password"]""").send_keys(self.PASSWORD)
        self.chrome_driver.find_element(By.XPATH, """//*[@id="organic-div"]/form/div[3]/button""").click()
        self.chrome_driver.find_element(By.XPATH, """//*[@id="global-nav"]/div/nav/ul/li[3]/a""").click()
        time.sleep(5)

    def search_by_job_type(self, job_type):
        """Posts in the search bar the type of job"""
        job_search_bar = self.chrome_driver.find_element(By.CSS_SELECTOR, ".relative input")
        job_search_bar.send_keys(job_type, Keys.ENTER)
        time.sleep(3)
        experience_level_button = self.chrome_driver.find_element(By.XPATH, """/html/body/div[5]/div[3]/div[
        4]/section/div/section/div/div/div/ul/li[4]/div/span/button""")
        experience_level_button.click()
        time.sleep(3)

    def search_with_experience_level(self, experience_level):
        """clicks on user experience level according to user output"""
        if experience_level == 1:
            internship = self.chrome_driver.find_element(By.XPATH, """/html/body/div[5]/div[3]/div[
            4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[1]/label""")
            internship.click()
        elif experience_level == 2:
            entry_level = self.chrome_driver.find_element(By.XPATH, """/html/body/div[5]/div[3]/div[
            4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[2]/label""")
            entry_level.click()
        elif experience_level == 3:
            associate = self.chrome_driver.find_element(By.XPATH, """/html/body/div[5]/div[3]/div[
            4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label""")
            associate.click()
        else:
            mid_level = self.chrome_driver.find_element(By.XPATH, """/html/body/div[5]/div[3]/div[
            4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[4]/label""")
            mid_level.click()

    def easy_apply(self):
        """Clicks on the easy apply button"""
        easy_apply_button = self.chrome_driver.find_element(By.XPATH, """/html/body/div[5]/div[3]/div[
        4]/section/div/section/div/div/div/ul/li[8]/div/button""")
        easy_apply_button.click()
        time.sleep(3)

    def apply_page_jobs(self):
        """Apply to all jobs on the page """
        counter = 1
        apply_counter = 0
        all_listings = self.chrome_driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
        for alist in all_listings:
            print(f"Applying.. Job - {counter}")
            counter += 1
            alist.click()
            time.sleep(2)

            apply_button = self.chrome_driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
            apply_button.click()
            time.sleep(2)
            # Cant Get this to work now :(
            # phone = self.chrome_driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text__input")
            # print(phone.)
            # if phone.text == "":
            #     phone.send_keys(self.PHONE_NUMBER)
            submit_button = self.chrome_driver.find_element(By.CSS_SELECTOR, "footer button")
            if submit_button.get_attribute("aria-label") == "Submit application":
                submit_button.click()
                apply_counter += 1
                print("Job application sent successfully")
                time.sleep(2)
                continue

            else:
                close_button = self.chrome_driver.find_element(By.XPATH, """/html/body/div[3]/div/div/button""")
                close_button.click()
                discard_button = self.chrome_driver.find_element(By.XPATH, """/html/body/div[3]/div[2]/div/div[
                3]/button[1]""")
                discard_button.click()
                print("Complex application, skipped.")
                time.sleep(2)
                continue
        print(f"Applied for {apply_counter} jobs.")





                                                                          