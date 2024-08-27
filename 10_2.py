import re

def first_word(text):
    """ Пошук першого слова """

    cleaned_text = re.sub(r'^[\s.,]+', '', text)

    match = re.match(r"[\w'-]+", cleaned_text)

    if match:
        return f'"{match.group(0)}"'

    return ''


print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))
print('OK')