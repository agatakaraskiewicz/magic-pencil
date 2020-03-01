class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def load(self, url):
        self.driver.get(url)
