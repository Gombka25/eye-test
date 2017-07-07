from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EyeGamePage:
    url = "http://igame.com/eye-test/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("Iframe"))

    def click_chosen_one(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".thechosenone").click()

    def get_current_time(self):
        return self.driver.find_element_by_css_selector('.clock').text

    def get_to_robot_level(self):
        for i in range(30):
            self.click_chosen_one()

        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.ID, "timeleft")))

    def get_reached_level(self):
        return self.driver.find_element_by_css_selector('.character-title').text