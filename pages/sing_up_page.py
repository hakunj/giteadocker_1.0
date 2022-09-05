from random import randint

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sing_up_page(Base):

    url = "http://localhost:3000/user/sign_up"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Селекторы"""

    user_name_bar_locator  = "//input[@id='user_name']"
    email_bar_locator = "//input[@id='email']"
    password_bar_locator = "//input[@id='password']"
    password2_bar_locator = "//input[@id='retype']"
    port_bar_locator = "//input[@id='password']"
    sing_up_btn = "//button[@class='ui green button']"
    page_header_locator = "//h3[@class='ui top attached header']"

    """Getters"""

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name_bar_locator)))

    def get_email_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_bar_locator)))

    def get_password_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_bar_locator)))

    def get_password2_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password2_bar_locator)))

    def get_sing_up_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sing_up_btn)))

    def get_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_header_locator)))

    """Actions"""

    def input_user_name(self, name):
        self.get_user_name().send_keys(name)
        print("Введено имя : " + name)

    def input_email(self, email):
        self.get_email_bar().send_keys(email)
        print("Введена почта : " + email)

    def input_password(self, pwrd):
        self.get_password_bar().send_keys(pwrd)
        print("Введен пароль : " + pwrd)

    def input_password2(self, pwrd):
        self.get_password2_bar().send_keys(pwrd)
        print("Введен повторно пароль : " + pwrd)

    def click_sing_up_btn(self):
        self.get_sing_up_btn().click()
        print("Нажата кнопка регистрации")


    """Methods"""

    def sign_up_ivan(self):
        self.driver.get(self.url)
        self.input_user_name("Ivan" + str(randint(0, 1000)))
        self.input_email("example" + str(randint(0, 1000)) + "@gmail.com")
        self.input_password("somepass123")
        self.input_password2("somepass123")
        # self.get_screenshot()
        self.click_sing_up_btn()
