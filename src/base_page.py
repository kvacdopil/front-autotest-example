from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)

        if not item.startswith('_') and not callable(attr):
            attr.driver = self.driver
            attr.page = self
        return attr

    def get(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url
    
    def go_back(self):
        self.driver.back()
        self.wait_page_loaded()
    
    def refresh_page(self):
        self.driver.refresh()
    
    def get_page_source(self):
        source = ''
        try:
            source = self._web_driver.page_source
        except:
            print('Can not get page source.')

        return source
