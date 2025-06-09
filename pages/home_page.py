from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_icon = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar > div")
        self.exit_btn = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(7)")
        self.confirm_exit_btn = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.coworking_btn = (By.CSS_SELECTOR, "#app > div > div.layout > div > div.material-dialog__window > div > ul > li:nth-child(2)")
        self.reserve_btn = (By.CSS_SELECTOR, "#app > div > div.coworking > div > button")

    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.profile_icon)).click()

    def click_exit_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.exit_btn)).click()

    def click_confirm_exit_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.confirm_exit_btn)).click()

    def click_coworking_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.coworking_btn)).click()

    def click_reserve_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.reserve_btn)).click()