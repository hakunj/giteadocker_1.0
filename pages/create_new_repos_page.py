from base.base_class import Base
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Create_new_repos_page(Base):

    url = "http://localhost:3000/repo/create"

    """Селекторы"""

    repo_name_locator  = "//input[@id='repo_name']"
    repo_init_locator  = "//*[@id='auto-init']/label"
    create_repo_locator = "//button[@class='ui green button']"

    """Getters"""

    def get_repo_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.repo_name_locator)))

    def get_repo_init(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.repo_init_locator)))

    def get_create_repo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create_repo_locator)))


    """Actions"""

    def input_repo_name(self, name):
        self.get_repo_name().send_keys(name)
        print("Имя нового репозитория : " + name)

    def click_repo_init(self):
        self.get_repo_init().click()
        print("Нажата галочка инициализации нового репозитория")

    def click_create_repo(self):
        self.get_create_repo().click()
        print("Нажата кнопка создания нового репозитория")




    """Methods"""

    def create_new_repos(self):
        self.input_repo_name("New_project_" + str(randint(0, 10000)))
        self.click_repo_init()
        self.click_create_repo()

