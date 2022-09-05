import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver


    """ Method get current url """

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий ulr " + get_url)

    """ Method assert word """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Текст совпадает " + value_word + " и " + result)

    """ Method screenshot """

    # def get_screenshot(self):
    #     now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.")
    #     name_screenshot = 'screenshot ' + now_date + 'png'
    #     self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\giteadocker_1.0\\screen\\' + name_screenshot)

    """ Method assert url """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Url совпадает")
