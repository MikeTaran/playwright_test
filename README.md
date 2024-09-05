## Инструкция запуска тестов:
### Локально:
1. Стянуть репу
2. Подтянуть зависимости: `python3 -m pip install -r requirements.txt`
3. После установки зависимостей прописать: `playwright install`
4. Создать файл .env в корневой директории и добавить значения переменным: `ENV=prod`,  `AUTH_LOGIN = standard_user`, `AUTH_PASSWORD = secret_sauce` (Актуально если нету файла .env)
5. Запустить тесты командой: `pytest` (по умолчанию тесты запустятся в Chrome). Для запуска только одной группы тестов использовать модуль `-m`: 
    + Регресс: `pytest -m regression`
    + Smoke: `pytest -m smoke`
    + Запуск отдельных тестов: нужно перейти в папку tests командой `cd tests` и запустить нужный тест командой  `pytest -s test_buy_product.py` (пример)


### --------------------------------
playwright codegen https://admin.websitewizard.ru/ --save-storage=auth.json
playwright codegen --load-storage=auth.json https://admin.websitewizard.ru/