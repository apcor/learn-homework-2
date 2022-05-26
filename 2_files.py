"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        ref_contents = f.read()
        print(f"The file's text is {len(ref_contents)} characters long.\n"\
            f"There are {len(ref_contents.split())} words in it.")
    
    ref_excl = ref_contents.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(ref_excl)


if __name__ == "__main__":
    main()
