def top_k_words(text: str, k: int):
    text = (text + '.').lower()
    words_dict = dict()
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
    sorted_dict = sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))
    return sorted_dict[0:k]


