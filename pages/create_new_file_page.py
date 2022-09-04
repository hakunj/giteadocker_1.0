from base.base_class import Base
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Create_new_file_page(Base):

    url = "http://localhost:3000/repo/create"
    some_text = "import selenium"
    """Селекторы"""

    file_name_locator  = "//input[@id='file-name']"
    text_bar_locator  = "//div[@class='view-lines monaco-mouse-cursor-text']"
    commit_btn_locator = "//button[@id='commit-button']"

    """Getters"""

    def get_file_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.file_name_locator)))

    def get_text_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_bar_locator)))

    def get_commit_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.commit_btn_locator)))


    """Actions"""

    def input_file_name(self, name):
        self.get_file_name().send_keys(name)
        print("Имя нового файла : " + name)

    def input_text_bar(self, some_text):
        self.get_text_bar().send_keys(some_text)
        print("Вы написали в новый файл : " + some_text)

    def click_commit_btn(self):
        self.get_commit_btn().click()
        print("Нажата кнопка 'Сохранить правки'")




    """Methods"""

    def create_new_file(self):
        self.input_file_name("new_file_" + str(randint(0, 10000)))
        self.input_text_bar(self.some_text)
        self.click_commit_btn()

