""" read   hardcoded values of config.ini file we use read properties file"""

import configparser

config = configparser.RawConfigParser()# configparser-> class,rowconfigparse->method
config.read(".\\configurations\\config.ini")# path of config.ini file

class Read_Config():
    @staticmethod
    def get_admin_url():
        url = config.get('admin','admin_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin','username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin','password')
        return password

    @staticmethod
    def get_wrong_email():
        wrong_email = config.get('admin','wrong_email')
        return wrong_email


