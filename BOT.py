from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import argparse

class InstagramBot():
    def __init__(self, email, password,username):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.ur = username

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def Change_Pic(self):
        self.browser.get('https://www.instagram.com/' + self.ur)
        inputs = self.browser.find_elements_by_xpath("//input[@accept = 'image/jpeg,image/png']")
        for inputt in inputs:
            inputt.send_keys(os.getcwd() + "/h.png")



ap = argparse.ArgumentParser()
ap.add_argument("-e", "--em", required=True, help="your Email")
ap.add_argument("-u", "--user", required=True, help="your user name")
ap.add_argument("-p", "--pasw", required=True, help="your password")

args = vars(ap.parse_args())

bot = InstagramBot(args["em"],args["pasw"],args["user"])
bot.signIn()
bot.Change_Pic()