import threading
import requests
import  time
import logging
logging.basicConfig(level=logging.DEBUG)


def save_content(url, file):
    logging.info(f"get url: {url}")
    rq = requests.get(url)
    logging.info(f"status={rq.status_code}")
    if rq.status_code == 200:
        logging.info(f"save to file: {file}")
        with open(file, "w", encoding='utf8') as file2save:
            print(rq.text, file=file2save)


thr = threading.Thread(target=save_content, args=('https://epam.com', '.\\epam.txt'))
thr.daemon = True
thr.start()

# Нужно дождаться завершения треда
time.sleep(5)

# save_content('https://epam.com', ".\\epam.txt")
