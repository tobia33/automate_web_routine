import os
from YoutubeShuffle import YoutubeShuffle
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import FirefoxProfile
from selenium.webdriver.firefox.options import Options

from youtube_support import execute_command
from youtube_exceptions import *
os.system("clear")
partial_welcome_string = "Welcome to Shuffle Manager!"
wrapping_lines = "#"*50 + "\n\t"

how_many_sx = (50 - 10 - len(partial_welcome_string))//2
how_many_dx = how_many_sx + len(partial_welcome_string)%2
welcome_string = "\n\t" + wrapping_lines*3 + "#"*how_many_sx + "-----" +\
    partial_welcome_string + "-----" + "#"*how_many_dx + "\n\t" + wrapping_lines*3
print(welcome_string)

options = Options()
if input("do you want the manual version?") == "y":
    manual = True
else:
    options.headless = True
    manual = False
#myprofile = FirefoxProfile("/home/tobia/.mozilla/firefox/iz1qwvqy.default-release")
#manager = YoutubeShuffle(Firefox(executable_path="/home/tobia/projects/useful_stuff/geckodriver", firefox_profile=myprofile, options=options))

manager = YoutubeShuffle(Firefox(executable_path="/home/tobia/projects/useful_stuff/geckodriver", options=options))
manager.goto()

manager.get_rid_of_cookies()
print("="*70)
print(">write help (or h) to get  the list of all commands and an explanation\n")
print(">write quick help (or qh) for a compact list of most used commands")
print("="*70 + "\n")
if manual:
    inp = input("choose one genre r or j")
    if inp == "j":
        manager.driver.get("https://www.youtube.com/user/BnFJazzBlues")
    else:
        manager.driver.get("https://www.youtube.com/c/ClassicRock26")

while True:
    print("-"*70)
    command = input("\nwhat can I do?\n\n>")
    if not command:
        continue
    elif command == "quit" or command == "q":
        manager.quit()
        break
    try:
        info = execute_command(manager, command)
        if info:
            print(info)
    except Exception as e:
        if isinstance(e, PickedSongNotFoundException):
            print("it seems the song you chose was not present, try again!")
            continue
        else:
            manager.driver.close()
            raise e
