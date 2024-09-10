def single_root_word(root_word, *other_word):
    same_words = []
    root_word = root_word.lower()
    other_word_low = [i.lower() for i in other_word]

    for i in other_word_low:
        if i in root_word or root_word in i:
            same_words.append(i)
    return same_words


result1 = single_root_word('rich', 'richest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_word('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)