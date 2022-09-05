from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logged_main_page(Base):

    url = "http://localhost:3000/"

    """Селекторы"""

    drop_down_btn_locator  = "//div[@data-content='Создать…']"
    new_repos_btn_locator = "//a[@id='_aria_auto_id_1']"

    """Getters"""

    def get_drop_down_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drop_down_btn_locator)))

    def get_new_repos_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_repos_btn_locator)))


    """Actions"""

    def click_drop_down_btn(self):
        self.get_drop_down_btn().click()
        print("Нажата кнопка для раскрытия меню")

    def click_new_repos_btn(self):
        self.get_new_repos_btn().click()
        print("Нажата кнопка url создания нового репозитория")




    """Methods"""

    def new_repos_navigate(self):
        self.click_drop_down_btn()
        self.click_new_repos_btn()

