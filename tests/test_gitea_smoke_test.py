import time
from selenium import webdriver
from base.base_class import Base
from selenium.common.exceptions import TimeoutException


from pages.create_new_file_page import Create_new_file_page
from pages.create_new_repos_page import Create_new_repos_page
from pages.installation_page import Installation_page
from pages.logged_main_page import Logged_main_page
from pages.main_page import Main_page
from pages.new_file_page import New_file_page
from pages.repos_page import Repos_page
from pages.sing_up_page import Sing_up_page

"""Включаем локальный сервер gitea с помощью фикстуры из docker-compose"""
def smoke_test_gitea_1(docker_services):

    """В путь необходимо вписать директорию к вашему chromedriver"""
    driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe')

    bc = Base(driver)
    print("Запуск теста gitea")
    ip = Installation_page(driver)
    mp = Main_page(driver)
    sup = Sing_up_page(driver)
    lmp = Logged_main_page(driver)
    crnp = Create_new_repos_page(driver)
    rp = Repos_page(driver)
    cnfp = Create_new_file_page(driver)
    nfp = New_file_page(driver)

    print("Проверка страницы начальной/инсталяции и создание скриншота")
    time.sleep(2)
    try:
        ip.install_default_options()
        bc.assert_word(ip.get_page_header(), "Начальная конфигурация")
        ip.click_primary_btn()
    except TimeoutException:
        try:
            driver.refresh()
            ip.install_default_options()
            ip.assert_word(ip.get_page_header(), "Начальная конфигурация")
            ip.click_primary_btn()
        except TimeoutException:
            driver.refresh()
            mp.check_main_page()
            mp.assert_word(mp.get_page_header(), "Gitea: Git with a cup of tea")
            mp.click_registration_btn()
    """Регистрируем нового пользователя"""
    sup.sign_up_ivan()
    """Переходим на страницу создания нового репозитория"""
    lmp.new_repos_navigate()
    """Создаем новый репозиторий"""
    crnp.create_new_repos()
    """Переходим на страницу создания нового файла"""
    rp.create_new_file_link()
    """Создаем новый файл"""
    cnfp.create_new_file()
    """Проверям текст"""
    bc.assert_word(cnfp.some_text, nfp.get_file_text())

    print("Тест пройден успешно.")



