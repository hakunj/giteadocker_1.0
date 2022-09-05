from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Repos_page(Base):


    """Селекторы"""

    add_file_btn_locator  = "//*[@id='file-buttons']/div/a[1]"
    # new_file_btn_locator  = "//a[@id='_aria_auto_id_12']"

    """Getters"""

    def get_add_file_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_file_btn_locator)))

    # def get_new_file_btn(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_file_btn_locator)))



    """Actions"""

    def click_add_file_btn(self):
        self.get_add_file_btn().click()
        print("Нажата кнопка добавления файла")

    # def click_new_file_btn(self):
    #     self.get_new_file_btn().click()
    #     print("Нажата кнопка создания нового файла")





    """Methods"""

    def create_new_file_link(self):
        self.click_add_file_btn()
        # self.click_new_file_btn()

