import codecs


def count_character_index(path: str):
    """
    Функция, подсчитывающая индекс частот появления букв и записывающая данную информацию в текстовый файл.
    """
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


def desipher(path: str, key: dict):
    """
    Дешифратор
    """
    f = codecs.open(u'' + path, "r", "utf-8")
    new_txt = ""
    for i in f.read():
        if i in key.keys():
            new_txt = new_txt + key[i]
        else:
            new_txt = new_txt + i
    f.close()
    print(new_txt)


desipher("original.txt", {"2": " ", "К": "О", "Ь": "И", "t": "Б", "Ы": "Р", "r": "Я", "Д": "C", ">": "С", "О": "Р",
                          "<": "В", "Б": "М", "Я": "Н", "Й": "Д", "1": "В", " ": "К", "Ч": "П", "0": "З", "М": "Ы",
                          "Х": "А", "А": "У", "a": "Ч", "Л": "Ж", "8": "Г", "c": "Х", "Е": "Ф", "3": "Й", ",": "Ю",
                          "b": "Б", ".": "Ц", "9": "Ш", "Ф": "Щ", "?": "Э"})

