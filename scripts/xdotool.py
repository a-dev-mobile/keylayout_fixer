import subprocess
import logging
import time

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f'Error running command {" ".join(command)}: {result.stderr}')
    return result

def simulate_keypress(key_sequence):
    logging.info(f'Simulating keypress: {key_sequence}')
    result = run_command(['xdotool', 'key', key_sequence])
    if result.returncode != 0:
        logging.error(f'Error simulating keypress: {result.stderr}')

def switch_layout():
    logging.info('Switching keyboard layout')
    result = run_command(['bash', 'scripts/switch_layout.sh'])
    if result.returncode != 0:
        logging.error(f'Error switching layout: {result.stderr}')

def type_text(text, delay=0.1):
    logging.info(f'Typing text: {text}')
    result = run_command(['xdotool', 'getactivewindow'])
    if result.returncode == 0:
        window_id = result.stdout.strip()
        logging.info(f'Setting focus to window {window_id}')
        run_command(['xdotool', 'windowfocus', '--sync', window_id])
        time.sleep(0.2)
    else:
        logging.error(f'Error getting active window: {result.stderr}')
        return
    
    result = run_command(['xdotool', 'type', '--delay', str(int(delay*1000)), text])
    if result.returncode != 0:
        logging.error(f'Error typing text "{text}": {result.stderr}')
    time.sleep(delay)
