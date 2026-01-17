def top_k_words(text: str, k: int):
    # добавляем небуквенный символ в конец для корректной обработки последнего слова
    text = (text + '.').lower()
    words_dict = dict()
    # флаг на новое слово
    is_new_word = True
    curr_word = ''
    for char in text:
        if is_new_word and char.isalpha():
            curr_word = char
            is_new_word = False
        elif not is_new_word and char.isalpha():
            curr_word = curr_word + char
        else:
            if curr_word in words_dict and curr_word != '':
                words_dict[curr_word] = words_dict[curr_word] + 1
            else:
                if curr_word != '':
                    words_dict[curr_word] = 1
            is_new_word = True
            curr_word = ''
    # непосредственная сортировка по условию задачи
    sorted_dict = sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))
    return sorted_dict[0:k]


print(top_k_words('One word', 10))
print(top_k_words('', 1))
print(top_k_words('normal, hard!!!!', 0))
print(top_k_words('типичное, предложение, странно, но.... но.... апельаНО!!! знаки,;;;стоят$странно', 3))
print(top_k_words('типичное, предложение, странно, но.... но.... апельаНО!!! знаки,;;;стоят$странно', 9))


