import re


def find_subtopics(text, language_of_work):
    """
    Функция find_subtopics извлекает главы и подглавы из текста на указанном языке.

    Принимает:
    - text (str): текстовый ответ от бота.
    - language_of_work (str): язык работы (1 - кыргызский, 2 - русский, 3 - английский).

    Возвращает:
    - subtopics (list): массив глав и подглав.
    """

    # Определение языка и соответствующих шаблонов и терминов
    language_data = {
        "1": {
            "intro": "Киришүү",
            "conclusion": "Корутунду",
            "references": "Колдонулган адабияттар",
            "patterns": [
                r'1-Бөлүм(.*?)(?=\n|\n$)', r'1.1(.*?)(?=\n|\n$)', r'1.2(.*?)(?=\n|\n$)', r'1.3(.*?)(?=\n|\n$)',
                r'2-Бөлүм(.*?)(?=\n|\n$)', r'2.1(.*?)(?=\n|\n$)', r'2.2(.*?)(?=\n|\n$)', r'2.3(.*?)(?=\n|\н$)'
            ]
        },
        "2": {
            "intro": "Введение",
            "conclusion": "Заключение",
            "references": "Список литературы",
            "patterns": [
                r'Глава 1(.*?)(?=\n|\н$)', r'1.1(.*?)(?=\n|\н$)', r'1.2(.*?)(?=\н|\н$)', r'1.3(.*?)(?=\н|\н$)',
                r'Глава 2(.*?)(?=\н|\н$)', r'2.1(.*?)(?=\н|\н$)', r'2.2(.*?)(?=\н|\н$)', r'2.3(.*?)(?=\н|\н$)'
            ]
        },
        "3": {
            "intro": "Introduction",
            "conclusion": "Conclusion",
            "references": "References",
            "patterns": [
                r'Chapter 1(.*?)(?=\н|\н$)', r'1.1(.*?)(?=\н|\н$)', r'1.2(.*?)(?=\н|\н$)', r'1.3(.*?)(?=\н|\н$)',
                r'Chapter 2(.*?)(?=\н|\н$)', r'2.1(.*?)(?=\н|\н$)', r'2.2(.*?)(?=\н|\н$)', r'2.3(.*?)(?=\н|\н$)'
            ]
        }
    }

    # Выбор данных для текущего языка
    data = language_data.get(language_of_work)
    if not data:
        return []

    subtopics = [data["intro"]]

    # Поиск текста для каждого шаблона
    for pattern in data["patterns"]:
        matches = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
        subtopics.extend(matches)

    subtopics.extend([data["conclusion"], data["references"]])

    # Удаление точек, двоеточий и звездочек в начале и конце каждого элемента
    subtopics = [subtopic.strip(" *.:") for subtopic in subtopics]

    return subtopics

