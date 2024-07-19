import re
import string


def first_word(text):
    """ Пошук першого слова """

    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group(0)
    return None



assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')


import string
def first_word(text):

    word = text.strip(string.punctuation).split()[0]
    final_word = ""
    for letter in word:
        if letter.isalpha() or letter == "'":
            final_word += letter
        elif letter in string.punctuation:
            break
    return final_word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')

