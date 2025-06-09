from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CoworkingPage:
    def __init__(self, driver):
        self.driver = driver
        self.second_branch = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-branch > div:nth-child(2) > div.list-tile.coworking__page-dialog-follow-branch-item-list > div.list-tile__trailing")
        self.choose_btn = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div:nth-child(1) > div.list-tile__trailing > button")
        self.next_btn = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.second_date = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-date > div > div:nth-child(4) > button")
        self.choose_group = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.list-tile.coworking__page-dialog-follow-list")
        self.choose_radio_btn_group = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div > div.list-tile__trailing > button")
        self.choose_group_btn = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.choose_time = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(1) > label > input")
        self.first_element = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(1) > input")
        self.second_element = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(2) > input")
        self.choose_time_btn = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.choose_place = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(2) > div")
        self.choose_number_place = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div.coworking__page-dialog-time-seats > div:nth-child(1)")
        self.choose_place_btn = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.send_btn = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")

    def click_second_branch(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.second_branch)).click()

    def click_choose_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.choose_btn)).click()

    def click_second_date(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.second_date)).click()

    def click_choose_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.choose_group)).click()

    def click_choose_radio_btn_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.choose_radio_btn_group)).click()

    def click_choose_group_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.choose_group_btn)).click()

    def click_next_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.next_btn)).click()

    def click_choose_time(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.choose_time)).click()

    def click_first_element(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.first_element))
        element.clear()
        element.send_keys("18")

    def click_second_element(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.second_element)).send_keys("30")

    def click_choose_time_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.choose_time_btn)).click()

    def click_choose_place(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.choose_place)).click()

    def click_choose_number_place(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.choose_number_place)).click()

    def click_choose_place_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.choose_place_btn)).click()

    def click_send_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.send_btn)).click()