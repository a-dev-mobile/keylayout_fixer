import sys
import os
import logging
from threading import Thread

# Добавляем родительскую директорию в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from keylayout_fixer.key_listener import start_key_listener
from keylayout_fixer.hotkey_handler import start_hotkey_listener

logging.basicConfig(filename='keylayout_fixer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    logging.info("Starting key layout fixer")
    Thread(target=start_key_listener).start()
    Thread(target=start_hotkey_listener).start()
    logging.info("Key layout fixer is running")
