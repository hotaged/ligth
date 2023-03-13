# Описание
В этом репозитории находится исходный код Python пакета
и SQL спроектированной БД
тестового задания от компании Own Script

## Содержание репозитория
- database
  - schema: Спроектированная БД и ее схема
  - scripts: Скрипты из пунктов 2
- flashlight - Пакет клиента фонаря 
- mock-flashlight-server - Примитивный сервер, эмулирующий поведение сервера фонаря

## Инструкция по запуску клиента фонаря
1. Установка модуля setuptools
    ```shell
    python -m pip install setuptools
    ```

2. Установка пакета клиента фонаря
    ```shell
    python setup.py install
    ```
   
3. Проверка установки
    ```shell
    flashlight --help
    ```
   Вывод должен выглядеть следующим образом:
    ```shell
    $ flashlight --help
    Usage: flashlight [OPTIONS]
    
    Options:
      --address TEXT  host:port of server to connect.
      --help          Show this message and exit.
    ```
4. Запуск с адресом по умолчанию (127.0.0.1:9999)
    ```shell
    flashlight
    ```

5. Запуск с иным адресом
    ```shell
    flashlight --address 192.168.3.103:9999
    ```
   
## Схема спроектированной базы данных

![alt text] (https://github.com/hotaged/ligth/blob/main/database/schema/public.png?raw=True)