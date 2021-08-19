from YoutubeShuffle import *
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

driver = Firefox(executable_path="/home/tobia/projects/useful_stuff/geckodriver")
a = YoutubeShuffle(driver)
a.goto()
a.get_rid_of_cookies()
a.find_recommended()
print(a.string_recommended())
a.pick_recommended(input())