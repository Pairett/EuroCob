# import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



# windows routes require
BROWSER_EXE = 'C:/Program Files/Mozilla Firefox/firefox.exe'
GECKODRIVER = './geckodriver.exe'
FIREFOX_BINARY = FirefoxBinary(BROWSER_EXE)

#  Code to disable notifications pop up of Browser
PROFILE = webdriver.FirefoxProfile()
# PROFILE.DEFAULT_PREFERENCES['frozen']['javascript.enabled'] = False
PROFILE.set_preference("dom.webnotifications.enabled", False)
PROFILE.set_preference("app.update.enabled", False)
# not load any images
PROFILE.set_preference("permissions.default.image", 2)
PROFILE.update_preferences()