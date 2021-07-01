import time

from notifier import Notifier
from variables import URL, EMAIL, PASSWORD


def main():
    while True:
        Notifier(URL, EMAIL, PASSWORD).start_cycle()
        
        time.sleep(60)


if __name__ == "__main__":
    main()
