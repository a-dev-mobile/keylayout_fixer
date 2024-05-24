import logging

def fix_layout(word):
    # Массивы русских и английских символов в разных регистрах
    ru_keys_lower = "йцукенгшщзхъфывапролджэячсмитьбю"
    ru_keys_upper = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    en_keys_lower = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    en_keys_upper = "QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>"

    # Создание таблиц перевода для каждой раскладки, сохраняя регистр
    ru_to_en = str.maketrans(ru_keys_lower + ru_keys_upper, en_keys_lower + en_keys_upper)
    en_to_ru = str.maketrans(en_keys_lower + en_keys_upper, ru_keys_lower + ru_keys_upper)

    # Определяем текущую раскладку
    is_ru_layout = all(char in ru_keys_lower + ru_keys_upper or not char.isalpha() for char in word)
    
    # Переводим в другую раскладку, сохраняя регистр
    if is_ru_layout:
        fixed_word = word.translate(ru_to_en)
        logging.info(f'Translating from RU to EN: {word} -> {fixed_word}')
    else:
        fixed_word = word.translate(en_to_ru)
        logging.info(f'Translating from EN to RU: {word} -> {fixed_word}')
    
    return fixed_word 