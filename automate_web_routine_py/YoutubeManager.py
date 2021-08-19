from SiteManager import SiteManager
from YoutubeSong import YoutubeSong
from selenium.webdriver import Firefox
from time import sleep



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
        sleep(1)
        button = self.driver.find_elements_by_css_selector("ytd-button-renderer.style-scope.ytd-consent-bump-v2-lightbox.style-primary.size-default")[1]
        button.click()

    def find_next_song(self):
        """ find the next song in queue """
        raw_next = self.driver.find_element_by_css_selector("ytd-compact-video-renderer, ytd-compact-radio-renderer")
        title = raw_next.find_element_by_id("video-title").get_attribute("textContent")
        url = raw_next.find_element_by_id("thumbnail").get_attribute("href")
        self.next_song = YoutubeSong(title.strip(), url)

    def string_next_song(self):
        return "\t-" + self.next_song.title

    def goto_next_song(self):
        """ go to the next song """
        self.current_song = self.next_song
        self.current_url = self.next_song.url
        self.next_song = None
        self.goto()
        self.play_pause()

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

    def back(self):
        super().back()
        self.play_pause()
        self.get_current_song()

    def forward(self):
        super().forward()
        self.play_pause()
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