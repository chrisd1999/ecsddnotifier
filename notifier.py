import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Notifier:

    def __init__(self, url, email, password):
        self.url = url
        self.email = email
        self.password = password
        self.driver = self.init_driver()
        self.open_url()

    def init_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--headless")
        return webdriver.Chrome(chrome_options=options)

    def open_url(self):
        self.driver.get(self.url)

    def login(self):
        login_field = (By.XPATH, '//*[@id="goLogin"]/a')
        email_field = (By.XPATH, '//*[@id="email"]')
        password_field = (By.XPATH, '//*[@id="psw"]')
        submit_field = (By.XPATH, '//*[@id="doLogin"]')

        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(login_field)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(email_field)).send_keys(self.email)
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(password_field)).send_keys(self.password)
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(submit_field)).click()

    def choose_field(self):
        valmiera_field = (By.XPATH, '//*[@id="nodala"]/option[10]')
        kvali_field = (By.XPATH, '//*[@id="6"]')
        l_field = (By.XPATH, '//*[@id="7"]')

        elements = [valmiera_field, kvali_field, l_field]
        for i in range(len(elements)):
            self.process_element(elements[i])

    def process_element(self, field):
        find_field = (By.XPATH, '//*[@id="find"]')

        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(field)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(find_field)).click()

    def time(self):
        find_field = (By.XPATH, '//*[@id="find"]')
        time_field = '//*[@id="laiks"]'
        date_change_field = (By.XPATH, '//*[@id="setdatums"]')

        for i in range(2, 6, 1):
            datumi_field = f'//*[@id="datums"]/option[{i}]'

            datumi_element = self.driver.find_element_by_xpath(datumi_field)
            print(datumi_element.text)

            WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, datumi_field))).click()
            WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(find_field)).click()

            select_box = self.driver.find_element_by_xpath(time_field)
            options = [x for x in select_box.find_elements_by_tag_name("option")]

            for idx, item in enumerate(options):
                if idx == 0:
                    continue
                print(item.text)

            WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(date_change_field)).click()

            time.sleep(5)

    def start_cycle(self):
        self.login()
        self.choose_field()
        self.time()
        self.quit()

    def quit(self):
        self.driver.quit()
