from selenium.webdriver import Firefox

class SiteManager:
    """ SiteManager manages a website
        with this class you can do basic operations shared by all sites"""

    __driver: Firefox

    def __init__(self, current_url, driver):
        """ constructor for SiteManager """
        self.__current_url = current_url
        driver.implicitly_wait(3)
        self.__driver = driver

    def goto(self):
        """ go to the current_url """
        self.driver.get(self.current_url)

    def back(self):
        """ click the back button"""
        self.driver.back()
        self.current_url = self.driver.current_url


    def forward(self):
        """ click the forward button """
        self.driver.forward()
        self.current_url = self.driver.current_url

    def refresh(self):
        """ click the refresh button """
        self.driver.refresh()

    def minimize(self):
        """ minimize the window """
        self.driver.minimize_window()

    def maximize(self):
        """ maximize the window """
        self.driver.maximize_window()

    @property
    def current_url(self):
        return self.__current_url

    @current_url.setter
    def current_url(self, value):
        self.__current_url = value

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, value):
        self.__driver = value