from selenium.webdriver import Edge


def get_driver():
    global driver
    if not driver:
        driver = Edge()
        driver.implicitly_wait(5)
    return driver()
