def popular_words(text, words):
    text_words = text.lower().split()

    word_count = {word: 0 for word in words}

    for word in text_words:
        if word in word_count:
            word_count[word] += 1
    return word_count

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')



def popular_words(text, words):
    text_words = text.lower().split()


    popular_dict_words = {}
    for word in words:
        popular_dict_words[word] = text_words.count(word)

    return popular_dict_words


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')


def popular_words(text, words):
    text_words = text.lower().split()

    return {word: text_words.count(word) for word in words} #dict comprehention

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')