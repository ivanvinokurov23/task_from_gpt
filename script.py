def top_k_words(text: str, k: int):
    # добавляем небуквенный символ в конец для корректной обработки последнего слова
    text = (text + '.').lower()
    words_dict = dict()
    # флаг на новое слово
    new_word = True
    curr_word = ''
    for char in text:
        if new_word and char.isalpha():
            curr_word = char
            new_word = False
        elif not new_word and char.isalpha():
            curr_word = curr_word + char
        else:
            if curr_word in words_dict and curr_word != '':
                words_dict[curr_word] = words_dict[curr_word] + 1
            else:
                if curr_word != '':
                    words_dict[curr_word] = 1
            new_word = True
            curr_word = ''
    # непосредственная сортировка по условию задачи
    sorted_dict = sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))
    return sorted_dict[0:k]


