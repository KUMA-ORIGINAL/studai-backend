import re


def find_subtopics(text, language_of_work):
    """
        Функция findsubtopics извлекает главы и подглавы из ответа ChatGPT.

        Принимает:
        - text (str): текстовый ответ от бота.
        - language_of_work (str): язык работы.

        Возвращает:
        - subtopics (list): массив глав и подглав.
    """

    subtopics = []
    # Если язык работы кыргызский
    if language_of_work == "1":
        # Шаблоны для поиска текста
        patterns = [
            r'1-Бөлүм(.*?)(?=\n|\n$)',  # Глава 1
            r'1.1(.*?)(?=\n|\n$)',  # Подразделения 1.1
            r'1.2(.*?)(?=\n|\n$)',  # Подразделения 1.2
            r'1.3(.*?)(?=\n|\n$)',  # Подразделения 1.3
            r'2-Бөлүм(.*?)(?=\n|\n$)',  # Глава 2
            r'2.1(.*?)(?=\n|\n$)',  # Подразделения 2.1
            r'2.2(.*?)(?=\n|\n$)',  # Подразделения 2.2
            r'2.3(.*?)(?=\n|\n$)',  # Подразделения 2.3
        ]


        subtopics.append("Киришүү")

        # Поиск текста для каждого шаблона
        for pattern in patterns:
            matches = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
            subtopics.extend(matches)

        subtopics.append("Корутунду")
        subtopics.append("Колдонулган адабияттар")

        # Удаление точек или двоеточий в начале каждого элемента
        subtopics = [subtopic.strip(" *.:") for subtopic in subtopics]

        return subtopics
    # Если язык работы русский
    elif language_of_work == "2":
        # Шаблоны для поиска текста
        patterns = [
            r'Глава 1(.*?)(?=\n|\n$)',  # Глава 1
            r'1.1(.*?)(?=\n|\n$)',  # Подразделения 1.1
            r'1.2(.*?)(?=\n|\n$)',  # Подразделения 1.2
            r'1.3(.*?)(?=\n|\n$)',  # Подразделения 1.3
            r'Глава 2(.*?)(?=\n|\n$)',  # Глава 2
            r'2.1(.*?)(?=\n|\n$)',  # Подразделения 2.1
            r'2.2(.*?)(?=\n|\n$)',  # Подразделения 2.2
            r'2.3(.*?)(?=\n|\n$)',  # Подразделения 2.3
        ]


        subtopics.append("Введение")

        # Поиск текста для каждого шаблона
        for pattern in patterns:
            matches = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
            subtopics.extend(matches)

        subtopics.append("Заключение")
        subtopics.append("Список литературы")

        # Удаление точек или двоеточий в начале каждого элемента
        subtopics = [subtopic.strip(" *.:") for subtopic in subtopics]

        return subtopics
    # Если язык работы английский
    elif language_of_work == "3":
        # Шаблоны для поиска текста
        patterns = [
            r'Chapter 1(.*?)(?=\n|\n$)',  # Глава 1
            r'1.1(.*?)(?=\n|\n$)',  # Подразделения 1.1
            r'1.2(.*?)(?=\n|\n$)',  # Подразделения 1.2
            r'1.3(.*?)(?=\n|\n$)',  # Подразделения 1.3
            r'Chapter 2(.*?)(?=\n|\n$)',  # Глава 2
            r'2.1(.*?)(?=\n|\n$)',  # Подразделения 2.1
            r'2.2(.*?)(?=\n|\n$)',  # Подразделения 2.2
            r'2.3(.*?)(?=\n|\n$)',  # Подразделения 2.3
        ]

        subtopics.append("Introduction")

        # Поиск текста для каждого шаблона
        for pattern in patterns:
            matches = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
            subtopics.extend(matches)

        subtopics.append("Conclusion")
        subtopics.append("References")

        # Удаление точек или двоеточий в начале каждого элемента
        subtopics = [subtopic.strip(" *.:-") for subtopic in subtopics]

        return subtopics

