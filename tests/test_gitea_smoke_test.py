import time
import pytest
from selenium import webdriver
from base.base_class import Base
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.installation_page import Installation_page
from pages.logged_main_page import Logged_main_page
from pages.main_page import Main_page
from pages.sing_up_page import Sing_up_page

"""Включаем локальный сервер gitea с помощью фикстуры docker-compose"""
def test_gitea_1(docker_services):

    """В путь необходимо вписать директорию к вашему chromedriver"""
    driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe')

    bc = Base(driver)
    print("Запуск теста gitea")
    ip = Installation_page(driver)
    mp = Main_page(driver)
    sup = Sing_up_page(driver)
    lmp = Logged_main_page(driver)
    print("Проверка страницы начальной/инсталяции и создание скриншота")
    time.sleep(3)
    try:
        ip.install_default_options()
        bc.get_screenshot()
        bc.assert_word(ip.get_page_header(), "Начальная конфигурация")
        ip.click_primary_btn()
    except TimeoutException:
        try:
            ip.install_default_options()
            ip.get_screenshot()
            ip.assert_word(ip.get_page_header(), "Начальная конфигурация")
            ip.click_primary_btn()
        except TimeoutException:
            driver.refresh()
            mp.check_main_page()
            mp.get_screenshot()
            mp.assert_word(mp.get_page_header(), "Gitea: Git with a cup of tea")
            mp.click_registration_btn()
    sup.sign_up_ivan()
    lmp.new_repos()

    time.sleep(90)

