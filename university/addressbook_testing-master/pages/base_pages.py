from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_element_visible(self, by, locator):
        try:
            self.wait.until(visibility_of_element_located((by, locator)))
            return True
        except WebDriverException:
            return False


class BasePage(Page):
    @property
    def logo(self):
        return self.driver.find_element_by_css_selector("#header > a > img")


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://localhost/addressbook/")
    base_page = BasePage(driver)
    print(base_page.logo.get_attribute("src"))
    base_page.logo.click()
    driver.quit()