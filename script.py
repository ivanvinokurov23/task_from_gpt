def top_k_words(text: str, k: int):
    text = text.lower()
    words = {}
    current = ""

    for char in text:
        if char.isalpha():
            current += char
        else:
            if current:
                words[current] = words.get(current, 0) + 1
                current = ""

    if current:
        words[current] = words.get(current, 0) + 1

    return sorted(words.items(), key=lambda x: (-x[1], x[0]))[:k]



print(top_k_words('One word', 10))
print(top_k_words('', 1))
print(top_k_words('normal, hard!!!!', 0))
print(top_k_words('типичное, предложение, странно, но.... но.... апельаНО!!! знаки,;;;стоят$странно', 3))
print(top_k_words('ЗЗтипичное, предложение, странно, но.... но.... апельаНО!!! знаки,;;;стоят$странно', 9))


