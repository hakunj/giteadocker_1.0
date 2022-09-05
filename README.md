### giteadocker_1.0
### Version 1.0
### Для запуска требуются Docker version 20.10.17(build 100c701),   python 3.8+, совместимые chrome и chrome driver.
### В  терминале прописываем 
- pip3 install pytest 
- pip3 install docker-compose
- pip3 install selenium 
### Перед запуском необходимо в test_gitea_smoke_test.py поменять пусть к драйверу и включить docker.
### Для запуска в терминале пишем  
> python -m pytest -s -v tests\test_gitea_smoke_test.py
### Для подключения скриншотов к тестам, надо поменять путь к папке со скриншотами, раскоммитить метод скриншотов в base\base_class.py и вызов функции в необходимых старницах.
### Тест подходит и для уже установленных репозиториев gitea
