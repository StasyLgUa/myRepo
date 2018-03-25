from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from pages.login_page import LoginPage
from pages.internal_page import InternalPage



class AddressbookApp:
    def __init__(self, base_url="http://localhost:8888/addressbook"):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = base_url
        self.driver.get(self.base_url)

        self.login_page = LoginPage(self.driver)
        self.internal_page = InternalPage(self.driver)




    def return_to_group_page(self):
        self.driver.find_element_by_link_text("group page").click()

    def create_group(self, group_name, group_header, group_footer):
        driver = self.driver
        # Initiate create group
        driver.find_element_by_name("new").click()
        # Enter group data
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group_name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group_header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group_footer)
        driver.find_element_by_name("submit").click()

    def open_group_page(self):
        self.driver.find_element_by_link_text("Группы").click()

    def logout(self):
        self.driver.find_element_by_link_text("Выйти").click()

    def login(self, username, password):
        self.login_page.username_field.clear()
        self.login_page.username_field.send_keys(username)

        self.login_page.password_field.clear()
        self.login_page.password_field.send_keys(password)

        self.login_page.submit_button.click()

    def delete_group(self, number):
        driver = self.driver
        checkboxes = driver.find_elements_by_name("selected[]")
        checkboxes[number].click()
        driver.find_element_by_name("delete").click()


    def message_group_confirm(self):
        mes = self.driver.find_element_by_css_selector("#content > div")
        return mes.text



    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close(self):
        self.driver.quit()
