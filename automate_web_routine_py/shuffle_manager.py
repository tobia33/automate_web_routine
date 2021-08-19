import os
from SiteManager import SiteManager
from YoutubeManager import YoutubeManager
from YoutubeSong import YoutubeSong
from YoutubeShuffle import YoutubeShuffle
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep
from youtube_support import execute_command
from youtube_exceptions import *
import sys

os.system("clear")
partial_welcome_string = "Welcome to Shuffle Manager!"
wrapping_lines = "#"*50 + "\n\t"

how_many_sx = (50 - 10 - len(partial_welcome_string))//2
how_many_dx = how_many_sx + len(partial_welcome_string)%2
welcome_string = "\n\t" + wrapping_lines*3 + "#"*how_many_sx + "-----" +\
    partial_welcome_string + "-----" + "#"*how_many_dx + "\n\t" + wrapping_lines*3
print(welcome_string)

manager = YoutubeShuffle(Firefox(executable_path="/home/tobia/projects/useful_stuff/geckodriver"))
manager.goto()

os.system("xdotool key alt+ctrl+shift+Right")
os.system("xdotool set_desktop --relative 1")

os.system("xdotool key alt+ctrl+t")
os.system("xdotool key alt+ctrl+t")

manager.get_rid_of_cookies()
print("="*70)
print(">write help (or h) to get  the list of all commands and an explanation\n")
print(">write quick help (or qh) for a compact list of most used commands")
print("="*70 + "\n")

while True:
    print("-"*70)
    command = input("\nwhat can I do?\n>")
    if command == "quit" or command == "q":
        manager.driver.close()
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
