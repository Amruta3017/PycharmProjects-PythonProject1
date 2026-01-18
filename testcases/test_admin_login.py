import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from base_pagespom.loginadmin_page import login_admin_page
from utility.custom_logger import Log_Maker
from utility.read_properties import Read_Config

class Test_01_admin_login():

    admin_url = Read_Config.get_admin_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    wrong_email = Read_Config.get_wrong_email()
    logger = Log_Maker.log_gen()# create log object

    def test_01_admin_login(self,setup):
        self.logger.info("**************test_01_admin_login****************")
        self.driver = setup
        print("Admin URL is:", self.admin_url)
        self.driver.get(self.admin_url)
        time.sleep(10)
        actual_title = self.driver.title
        print(actual_title)
        expected_title = "nopCommerce demo store. Login"

        if actual_title == expected_title:
            assert True
            self.logger.info("**************title match****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screensots\\test_01_admin_login.png")
            self.driver.close()
            self.logger.info("**************title not match****************")
            assert False

    def test_02_valid_admin_login(self,setup):
        self.logger.info("**************test_02_valid_admin_login****************")
        self.driver = setup
        self.driver.get(self.admin_url)
        self.admin_lp = login_admin_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/h1").text
        if actual_dashboard_text == "admin-demo.nopcommerce.com":
            assert True
            self.logger.info("**************login successfull****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screensots\\test_02_valid_admin_login.png")
            self.logger.info("**************login not successfull****************")
            self.driver.close()
            assert False


    def test_03_invalid_admin_login(self,setup):
        self.logger.info("**************test_03_invalid_admin_login****************")
        self.driver = setup
        self.driver.get(self.admin_url)
        self.admin_lp = login_admin_page(self.driver)
        self.admin_lp.enter_username(self.wrong_email)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_msg_text = self.driver.find_element(By.XPATH,"//li").text
        if error_msg_text == "No customer account found":
            assert True
            self.logger.info("**************invalid login****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screensots\\test_03_invalid_admin_login.png")
            self.driver.close()
            self.logger.info("**************invalid login error****************")
            assert False
