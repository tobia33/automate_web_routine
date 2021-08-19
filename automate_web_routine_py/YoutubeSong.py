class YoutubeSong:
    """ YoutubeSong represents a youtube song"""

    def __init__(self, title, url):
        """ constructor for YoutubeSong """
        self.__title = title
        self.__url = url

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
