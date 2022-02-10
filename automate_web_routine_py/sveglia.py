from YoutubeShuffle import YoutubeShuffle
from youtube_support import execute_command
from youtube_exceptions import *
from selenium.webdriver import Firefox
from time import sleep

while True:
    manager = YoutubeShuffle(Firefox(executable_path="/home/tobia/projects/useful_stuff/geckodriver"))
    manager.current_url = "https://www.youtube.com/watch?v=U_M7w6JtHrk"
    manager.goto()
    manager.get_rid_of_cookies()
    if manager.ad_checker():
        done = manager.ad_killer()
    if not done:
        manager.quit()
        continue
    else:
        duration = manager.driver.find_element_by_class_name("ytp-time-duration").text
        minuti, secs = duration.split(":")
        sleep(minuti*60 + secs)
        manager.quit()
        break

