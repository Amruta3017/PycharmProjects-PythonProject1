
from selenium.webdriver.common.by import By


class login_admin_page:

    username_id = "Email"

    password = "Password"

    btn_login = '//*[@type="submit"]'

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login).click()