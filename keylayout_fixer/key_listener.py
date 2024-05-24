import logging
from pynput import keyboard
from .layout_fixer import fix_layout

logging.basicConfig(filename='keylayout_fixer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

typed_word = ""

def on_press(key):
    global typed_word
    try:
        if hasattr(key, 'char') and key.char is not None:
            logging.info(f'Alphanumeric or symbol key pressed: {key.char}')
            if key.char.isalnum() or key.char in ['\\', '/', '-', '=', '[', ']', ';', '\'', ',', '.', '`']:
                typed_word += key.char
                logging.info(f'Typed word: {typed_word}')
            elif key == keyboard.Key.space:
                fixed_word = fix_layout(typed_word)
                logging.info(f'Word typed: {typed_word} -> {fixed_word}')
                print(fixed_word, end=' ', flush=True)
                typed_word = ""
        else:
            logging.info(f'Special key pressed: {key}')
    except AttributeError:
        logging.error(f'Error in key press: {key}')

def start_key_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
