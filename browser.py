from selenium.webdriver import Edge


def get_driver():
    driver = Edge()
    driver.implicitly_wait(5)
    return driver()