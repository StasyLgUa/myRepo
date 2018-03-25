from pages.internal_page import InternalPage


class GroupViewPage(InternalPage):
    @property
    def group_checkboxes(self):
        return self.driver.find_element_by_name(self, "")
