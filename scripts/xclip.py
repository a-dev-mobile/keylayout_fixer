import subprocess
import logging


def paste_from_clipboard():
    try:
        result = subprocess.check_output(['xclip', '-selection', 'clipboard', '-o']).decode('utf-8')
        logging.info(f'Pasted from clipboard: {result}')
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f'Error pasting from clipboard: {e}')
        return ''

def paste_from_primary():
    try:
        result = subprocess.check_output(['xclip', '-selection', 'primary', '-o']).decode('utf-8')
        logging.info(f'Pasted from primary: {result}')
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f'Error pasting from primary: {e}')
        return ''
