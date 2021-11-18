import os
import logging
logging.basicConfig(level=logging.DEBUG)


def dir_print(path):
    logging.debug("-- Start function --")
    logging.debug(f"Check path: {path}")
    if not os.path.exists(path):
        logging.error(f"path not found: {path}")
    elif not os.path.isdir(path):
        logging.error(f"is not directory: {path}")
    else:
        logging.info(f"list dir")
        cnt = {'dir': 0, 'file': 0, 'ups': 0}
        for item in os.listdir(path=path):
            print(item)
            if os.path.isdir(f"{path}\\{item}"):
                cnt['dir'] += 1
            elif os.path.isfile(f"{path}\\{item}"):
                cnt['file'] += 1
            else:
                cnt['ups'] += 1
        logging.info(f"dir={cnt['dir']}, file={cnt['file']}" + (f"other={cnt['ups']}" if cnt['ups'] else ''))
    logging.debug("-- End function --")


dir_print("C:\\Programs")

dir_print("C:\\windows\\system31")

dir_print("C:\\windows\\system32")
