import logging
from pynput import keyboard
from scripts import xclip, xdotool
from .layout_fixer import fix_layout

logging.basicConfig(filename='keylayout_fixer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def on_activate_switch_layout():
    xdotool.switch_layout()

def on_activate_change_selected_text_layout():
    logging.info('Changing layout of selected text')
    # Get the text from primary selection
    selected_text = xclip.paste_from_primary()
    logging.info(f'Selected text for layout change: {selected_text}')
    # Fix the layout
    new_text = fix_layout(selected_text)
    logging.info(f'Changed text layout: {new_text}')
    # Simulate delete (cut) to remove the selected text
    xdotool.simulate_keypress('BackSpace')
    # Simulate typing the new text with delay
    xdotool.type_text(new_text, delay=0.1)
    
    xdotool.switch_layout()

def start_hotkey_listener():
    with keyboard.GlobalHotKeys({
       '<ctrl>+<shift>': on_activate_switch_layout,
       '<alt>+b': on_activate_change_selected_text_layout
    }) as listener:
        listener.join()
