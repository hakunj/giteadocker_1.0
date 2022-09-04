from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page(Base):

    url = "http://localhost:3000/"

    """Селекторы"""

    source_code_url_locator  = "//a[@href='https://code.gitea.io/gitea']"
    docker_url_btn_locator = "//a[@href='https://github.com/go-gitea/gitea/tree/master/docker']"
    golang_url_btn_locator = "//a[@href='http://golang.org/']"
    registration_btn = "//a[@href='/user/sign_up']"
    page_header_locator = "//h1[@class='ui icon header title']"

    """Getters"""

    def get_source_code_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.source_code_url_locator)))

    def get_docker_url_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.docker_url_btn_locator)))

    def get_golang_url_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.golang_url_btn_locator)))

    def get_registration_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_btn)))

    def get_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_header_locator)))

    """Actions"""

    def exist_source_code_url(self):
        self.get_source_code_url()
        print("Кнопка с url к исходному коду существует")

    def exist_docker_url_btn(self):
        self.get_docker_url_btn()
        print("Кнопка с url к docker существует")

    def exist_golang_url_btn(self):
        self.get_golang_url_btn()
        print("Кнопка с url к golang существует")

    def click_registration_btn(self):
        self.get_registration_btn().click()
        print("Нажата кнопка установки параметров gitea")


    """Methods"""

    def check_main_page(self):
        self.driver.get(self.url)
        self.exist_source_code_url()
        self.exist_golang_url_btn()
        self.exist_docker_url_btn()
        self.get_screenshot()
        self.click_registration_btn()
