import codecs


def count_character_index(path: str):
    '''
    Функция, подсчитывающая индекс частот появления букв и записывающая данную информацию в текстовый файл.
    '''
    letter_counter = {}
    absolute_character_counter = 0
    f = codecs.open(u'' + path, "r", "utf-8")
    for i in f.read():
        if i in letter_counter.keys():
            letter_counter[i] += 1
            absolute_character_counter += 1
        else:
            letter_counter[i] = 1
            absolute_character_counter += 1
    print(letter_counter)
    f.close()
    f = codecs.open(u''+"indx.txt", "w", "utf-8")
    for i in letter_counter.keys():
        f.write(i + ":" + str(letter_counter[i]/absolute_character_counter) + "\n")
    f.close()


count_character_index("original.txt")

