from base.base_class import Base
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class New_file_page(Base):

    url = "http://localhost:3000/repo/create"
    some_text = "import selenium"
    """Селекторы"""

    file_text_locator  = "//code[@class='code-inner']"

    """Getters"""

    def get_file_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.file_text_locator)))




    """Actions"""








    """Methods"""



