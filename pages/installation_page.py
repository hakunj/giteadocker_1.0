from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Installation_page(Base):

    url = "http://localhost:3000/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Селекторы"""

    app_name_bar_locator  = "//input[@id='app_name']"
    root_path_bar_locator = "//input[@id='lfs_root_path']"
    domain_bar_locator = "//input[@id='domain']"
    port_bar_locator = "//input[@id='http_port']"
    primary_btn = "//button[@class='ui primary button']"
    page_header_locator = "//h3[@class='ui top attached header']"

    """Getters"""

    def exist_of_app_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.app_name_bar_locator)))

    def get_root_path_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.root_path_bar_locator)))

    def get_domain_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.domain_bar_locator)))

    def get_port_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.port_bar_locator)))

    def get_primary_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.primary_btn)))

    def get_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_header_locator)))

    """Actions"""

    def exist_app_name_bar(self):
        self.exist_of_app_name()
        print("Поле ввода имени существует")

    def click_root_path_bar(self):
        self.get_root_path_bar().click()
        print("Нажато поле ввода корневой папки")

    def click_domain_bar(self):
        self.get_domain_bar().click()
        print("Нажато поле ввода домена")

    def click_port_bar(self):
        self.get_port_bar().click()
        print("Нажато поле ввода порта")

    def click_primary_btn(self):
        self.get_primary_btn().click()
        print("Нажата кнопка установки параметров gitea")


    """Methods"""

    def install_default_options(self):
        self.driver.get(self.url)
        self.exist_app_name_bar()
        self.click_domain_bar()
        self.click_root_path_bar()
        self.click_port_bar()
        self.get_screenshot()
        self.click_primary_btn()
