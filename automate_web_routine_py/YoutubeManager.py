from SiteManager import SiteManager
from YoutubeSong import YoutubeSong
from selenium.common.exceptions import TimeoutException
import os
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By

class YoutubeManager(SiteManager):
    """ YoutubeManager manages the youtube website
        with this class you can manage the video"""

    __next_song: YoutubeSong
    __current_song: YoutubeSong

    def __init__(self, driver):
        """ constructor for YoutubeManager """
        self.__base_url = "https://www.youtube.com"
        super(YoutubeManager, self).__init__(self.__base_url, driver)
        self.__current_song = None
        self.__next_song = None

    def get_rid_of_cookies(self):
        """ get rid of the cookies when you start youtube """
        button = self.driver.find_elements_by_css_selector("ytd-button-renderer.style-scope.ytd-consent-bump-v2-lightbox.style-primary.size-default")[1]
        #sleep(0.3)
        button.click()

    def find_next_song(self):
        """ find the next song in queue """
        raw_next = self.driver.find_element_by_css_selector("ytd-compact-video-renderer, ytd-compact-radio-renderer")
        title = raw_next.find_element_by_id("video-title").get_attribute("textContent")
        url = raw_next.find_element_by_id("thumbnail").get_attribute("href")
        self.next_song = YoutubeSong(title.strip(), url)

    def string_next_song(self):
        return self.string_song(self.next_song)

    def string_current_song(self):
        return self.string_song(self.current_song)

    def string_song(self, song):
        return "\t-" + song.title

    def ad_checker(self):
        try:
            self.driver.find_element_by_class_name("ytp-ad-preview-container")
            return True
        except Exception as e:
            e.with_traceback()
            return False

    def ad_killer(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button")))
        except TimeoutException:
            return False
        self.driver.find_element_by_class_name("ytp-ad-skip-button").click()
        return True

    def goto_next_song(self):
        """ go to the next song """
        self.current_song = self.next_song
        self.current_url = self.next_song.url
        self.next_song = None
        self.goto()
        #sleep(0.5)
        self.play_pause()

    def go(self):
        """ go to the other workspace and look at the youtube page
            or come back"""
        os.system("xdotool set_desktop --relative 1")
        os.system("xdotool key alt+ctrl+t")
        os.system("xdotool key alt+ctrl+t")

    def play_pause(self):
        """ pause or resume the video """
        body = self.driver.find_element_by_tag_name("body")
        body.send_keys("k")

    def mute(self):
        """ mute the volume of the video """
        body = self.driver.find_element_by_tag_name("body")
        body.send_keys("m")

    def get_current_song(self):
        """ manually set current song when the song change
            is forced, (e.g. back, forward)"""
        self.current_song = YoutubeSong(self.driver.title, self.current_url)

    def quit(self):
        home_dir = os.listdir("/home/tobia")
        if "geckodriver.log" in home_dir:
            os.system("rm /home/tobia/geckodriver.log")
        self.driver.close()

    def back(self):
        super().back()
        self.get_current_song()

    def forward(self):
        super().forward()
        self.get_current_song()

    @property
    def current_song(self):
        return self.__current_song

    @current_song.setter
    def current_song(self, value):
        self.__current_song = value

    @property
    def next_song(self):
        return self.__next_song

    @next_song.setter
    def next_song(self, value):
        self.__next_song = value

    @property
    def base_url(self):
        return self.__base_url
