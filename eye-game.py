from selenium.webdriver import Edge
from selenium.webdriver.remote.webdriver import WebDriver

class EyeGamePage:

    url = "http://igame.com/eye-test/"

    def __init__(self, driver : WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("Iframe"))
        element = self.driver.find_element_by_class_name("thechosenone")