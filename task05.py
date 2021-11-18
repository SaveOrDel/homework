import sqlite3
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.DEBUG)


# 1. Работа с HTML
# Скачать содержимое страницы https://epam.com с помощью requests
# Посчитать количество тегов div на этой странице (лучше использовать для этого библиотеку beautifulsoup4)
def html_div_count(url):
    logging.info(f"get url: {url}")
    rq = requests.get(url)
    logging.info(f"status={rq.status_code}")
    logging.debug(f"content type ={rq.headers['Content-Type']}")
    if rq.status_code == requests.codes.ok:
        logging.info(f"Count tag div")
        soup = BeautifulSoup(rq.text, 'html.parser')
        tag = soup.find_all('div')
        print(f"tag div count = {len(tag)}")


html_div_count('https://epam.com')


# 2. Базы данных
# Работа с sqlite.
# С помощью SQL запросов создать таблицу содержаюую 2 стобца: номер и имя
# Добавить три строки с данными.
# Получить данные из таблицы и распечатать их на экране.
def sql_test():
    conn = sqlite3.connect(':memory:')
    sql = conn.cursor()
    sql.execute("CREATE TABLE people " +
                "(id int, name text)")
    sql.execute("INSERT INTO people VALUES (1,'Mark')")
    sql.execute("INSERT INTO people VALUES (2,'Bill')")
    sql.execute("INSERT INTO people VALUES (3,'Nikolas')")
    conn.commit()

    print("id\tname")
    print("__\t____")
    for row in sql.execute("select * from people order by id"):
        print(f"{row[0]}\t{row[1]}")


sql_test()