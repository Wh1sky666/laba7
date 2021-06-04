#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('me.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    # Заменить символы конца предложения.
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    # Удалить все многоточия.
    while ".." in text:
        text = text.replace("..", ".")
    # Разбить текст на предложения.
    sentences = text.split(".")
    words = text.split(" ")
    # Вывод предложений с запятыми.
    word = (input("Введите слово - "))
    print(text)
    i =0

    d = 0
    k= 1
    for sentence in sentences:
            r= 0
            for words in sentence:

                if word in words:
                    r += 1
            print(" --- ",sentence,r)
