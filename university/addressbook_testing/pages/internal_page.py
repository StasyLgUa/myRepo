from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InternalPage(BasePage):
    @property
    def main_menu(self):
        return

    @property
    def add_contact_menu(self):
        return

    @property
    def group_menu(self):
        return self.driver.find_element_by_link_text("Группы")

    def is_this_page(self):
        return self.is_element_present(By.CSS_SELECTOR,"#nav")

    def logout(self):
        pass