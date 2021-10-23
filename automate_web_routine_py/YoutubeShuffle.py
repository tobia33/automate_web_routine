from typing import List, Any
from SiteManager import SiteManager
from YoutubeManager import YoutubeManager
from YoutubeSong import YoutubeSong
from time import sleep
from random import randint
from youtube_exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By


class YoutubeShuffle(YoutubeManager):
    
    __found: list[YoutubeSong]
    __recommended: list[YoutubeSong]

    def __init__(self, driver):
        super(YoutubeShuffle, self).__init__(driver)
        self.__recommended = []
        self.__found = []

    def find_recommended(self):
        """ find the recommended songs """
        self.recommended = []
        if self.current_url == self.base_url:
            raw_recommended = self.driver.find_elements_by_css_selector("ytd-rich-item-renderer")
        else:
            raw_recommended = self.driver.find_elements_by_css_selector(
                "ytd-compact-video-renderer, ytd-compact-radio-renderer")
        for raw_song in raw_recommended:
            title = raw_song.find_element_by_id("video-title").get_attribute("textContent")
            url = raw_song.find_element_by_id("thumbnail").get_attribute("href")
            self.recommended.append(YoutubeSong(title.strip(), url))

    def search(self, string):
        """ search for the string in the search bar
            and put what is found in the found attribute"""
        self.found = []
        self.driver.get(self.base_url)
        search_bar = self.driver.find_element_by_css_selector("input#search")
        send = ""
        for c in string:
            if c == " ":
                search_bar.send_keys(send)
                search_bar.send_keys(Keys.SPACE)
                send = ""
            else:
                send += c
        search_bar.send_keys(send)
        wait = WebDriverWait(self.driver, 2)
        button = wait.until(element_to_be_clickable((By.CSS_SELECTOR, "button#search-icon-legacy")))
        button.click()
        self.current_url = self.driver.current_url
        self.current_song = None
        self.next_song = None
        sleep(1)
        raw_songs = self.driver.find_elements_by_css_selector("ytd-video-renderer")
        for raw_song in raw_songs:
            title = raw_song.find_element_by_id("video-title").get_attribute("textContent")
            url = raw_song.find_element_by_id("thumbnail").get_attribute("href")
            self.found.append(YoutubeSong(title.strip(), url))

    def string_show(self, iterable):
        """ used for string_recommended and string_found """
        to_show = ""
        for song in reversed(iterable):
            to_show += "\n" + self.string_song(song)
        return to_show

    def string_recommended(self):
        """ return a string containing the recommended songs """
        return self.string_show(self.recommended)

    def string_found(self):
        """ return a string containing the found songs """
        return self.string_show(self.found)

    def pick_from(self, string, iterable):
        """ used for string_recommended and string_found """
        length = len(string)
        for song in iterable:
            pieces = string.split()
            if song.title[:length] == string or all(list(map(lambda x: x in song.title, pieces))):
                self.next_song = song
                self.goto_next_song()
                break
        else:
            self.back()
            raise PickedSongNotFoundException()

    def pick_recommended(self, string):
        """ pick one of the recommended songs """
        self.pick_from(string, self.recommended)

    def pick_found(self, string):
        """ pick one of the found songs """
        self.pick_from(string, self.found)
    def shuffle(self):
        """ pick a random song among the ones in recommended """
        randy = randint(0, len(self.recommended)-1)
        self.next_song = self.recommended[randy]
        self.goto_next_song()

    @property
    def recommended(self):
        return self.__recommended

    @recommended.setter
    def recommended(self, value):
        self.__recommended = value

    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, value):
        self.__found = value
