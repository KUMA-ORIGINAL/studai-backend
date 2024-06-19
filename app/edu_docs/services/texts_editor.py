from nltk.tokenize import sent_tokenize
import nltk
import re

# Убедитесь, что необходимые ресурсы NLTK загружены
nltk.download('punkt')

def texts_editor(subtopic_texts, subtopics):
    """
        Функция textseditor редактирует тексты.

        Принимает:
        - subtopic_texts (list): массив текстов для подтем.
        - subtopics (list): массив подтем.

        Возвращает:
        - new_subtopic_texts (list): отредактированный массив текстов для подтем.

        Функция выполняет следующие действия:
        - Удаляет дубликаты предложений с помощью функции remove_duplicate_sentences.
        - Удаляет незавершенные предложения с помощью функции remove_incomplete_last_sentences.
        - Удаляет подглавы и главы, если они находятся в начале текста, с помощью функции remove_subtopic_headers.
        - Редактирует список литературы с помощью функции extract_bibliography.
        - Удаляет определенные символы ("**", "#").
    """

    new_subtopic_texts = []
    old_subtopic_texts = subtopic_texts
    print("Удаляем повторяющиеся предложения\n\n")
    for i in range(8):
        print(f"Оригинальный текст {i}:")
        print(old_subtopic_texts[i])
        print(f"Длина: {len(old_subtopic_texts[i])}\n\n")

        result, duplicates = remove_duplicate_sentences(old_subtopic_texts[i])

        old_subtopic_texts[i] = result

        print(f"Обработанный текст {i}:")
        print(old_subtopic_texts[i])
        print(f"Длина: {len(old_subtopic_texts[i])}\n\n")

        if duplicates:
            print(f"Повторяющиеся предложения в тексте {i}:")
            for sentence in duplicates:
                print(f"- {sentence}")
            print("\n\n")
        else:
            print(f"Повторяющихся предложений не найдено в тексте {i}.\n\n")

    print("\n\n\n\n\n\n\n\nУдаляем незавершенные предложения\n\n")

    for i in range(8):
        print(f"Оригинальный текст {i}:")
        print(old_subtopic_texts[i])
        print(f"Длина: {len(old_subtopic_texts[i])}\n\n")

        result, incomplete = remove_incomplete_last_sentences(old_subtopic_texts[i])
        old_subtopic_texts[i] = result

        print(f"Обработанный текст {i}:")
        print(old_subtopic_texts[i])
        print(f"Длина: {len(old_subtopic_texts[i])}\n\n")

        if incomplete:
            print(f"Незавершенные предложения в тексте {i}:")
            for sentence in incomplete:
                print(f"- {sentence}")
            print("\n\n")
        else:
            print(f"Незавершенных предложений не найдено в тексте {i}.\n\n")


    print("\n\n\n\n\n\n\n\nУдаляем подглавы, если они есть в начале текста\n\n")

    result, removed = remove_subtopic_headers(subtopics, old_subtopic_texts)
    for i, text in enumerate(result):
        print(f"Текст {i + 1}:")
        print(text)
        print("\n")
    old_subtopic_texts = result
    print("Удаленные подглавы:")
    for subtopic in removed:
        print(f"- {subtopic}")



    print("\n\n\n\n\n\n\n\nУдаляем лищние тексты из список литературы\n\n")

    new_bibliography_text = extract_bibliography(subtopic_texts[8])
    print(subtopic_texts[8])


    old_subtopic_texts.append(new_bibliography_text)

    print("\n\n\n\n\n\n\n\nУдаляем '**' и '#' в тексте, если есть\n\n")

    new_result = remove_asterisks(old_subtopic_texts)
    old_subtopic_texts = new_result

    new_subtopic_texts = old_subtopic_texts

    for new_text in new_subtopic_texts:
        print(new_text + "\n\n")


    return new_subtopic_texts

def remove_duplicate_sentences(text):
    """
        Функция remove_duplicate_sentences удаляет дубликаты предложений из текста.

        Принимает:
        - text (str): исходный текст.

        Возвращает:
        - result_text (str): текст без дубликатов предложений.
        - duplicate_sentences (list): массив удаленных дублирующихся предложений.
    """

    # Разделение текста на абзацы
    paragraphs = text.split('\n')

    all_sentences = []
    for paragraph in paragraphs:
        # Разделение абзаца на предложения
        sentences = sent_tokenize(paragraph)
        all_sentences.extend(sentences)

    # Удаление дубликатов с учётом нумерации и длины предложений
    seen_sentences = set()
    unique_sentences = []
    duplicate_sentences = []

    for sentence in all_sentences:
        # Проверка, является ли предложение нумерованным или коротким
        if re.match(r'^\d+\.\s', sentence) or len(sentence) <= 5:
            unique_sentences.append(sentence)
        else:
            if sentence not in seen_sentences:
                seen_sentences.add(sentence)
                unique_sentences.append(sentence)
            else:
                duplicate_sentences.append(sentence)

    # Разбиение уникальных предложений обратно на абзацы, сохраняя оригинальные абзацы
    result_paragraphs = []
    unique_sentence_index = 0

    for paragraph in paragraphs:
        sentences = sent_tokenize(paragraph)
        new_paragraph = []

        for _ in sentences:
            if unique_sentence_index < len(unique_sentences):
                new_paragraph.append(unique_sentences[unique_sentence_index])
                unique_sentence_index += 1

        result_paragraphs.append(' '.join(new_paragraph))

    # Соединение абзацев обратно в текст с сохранением переносов строк
    result_text = '\n'.join(result_paragraphs)
    return result_text, duplicate_sentences

def remove_incomplete_last_sentences(text):
    """
        Функция remove_incomplete_last_sentences удаляет незавершенные предложения из текста.

        Принимает:
        - text (str): исходный текст.

        Возвращает:
        - result_text (str): текст без незавершенных предложений.
        - incomplete_sentences (list): массив удаленных незавершенных предложений.
    """

    # Разделение текста на абзацы
    paragraphs = text.split('\n')

    result_paragraphs = []
    incomplete_sentences = []

    for paragraph in paragraphs:
        # Разделение абзаца на предложения
        sentences = sent_tokenize(paragraph)

        # Проверка последнего предложения
        if sentences and not re.search(r'[.!?:]$', sentences[-1].strip()):
            # Если последнее предложение незавершённое, сохраняем его для вывода
            incomplete_sentences.append(sentences[-1])
            # Удаляем последнее предложение
            sentences = sentences[:-1]

        # Соединение оставшихся предложений обратно в абзац
        result_paragraphs.append(' '.join(sentences))

    # Соединение абзацев обратно в текст с сохранением переносов строк
    result_text = '\n'.join(result_paragraphs)
    return result_text, incomplete_sentences

def remove_subtopic_headers(subtopics, subtopic_texts):
    """
        Функция remove_subtopic_headers удаляет подглавы и главы из начала текста.

        Принимает:
        - subtopics (list): массив подглав.
        - subtopic_texts (list): массив текстов для подглав.

        Возвращает:
        - updated_texts (list): обновленный массив текстов без подглав в начале.
        - removed_subtopics (list): массив удаленных подглав.
    """

    # Создаем список для хранения измененных текстов
    updated_texts = []
    # Создаем список для хранения подглав, которые были удалены
    removed_subtopics = []

    # Проходимся по каждому тексту в списке subtopic_texts
    for i in range(8):
        text = subtopic_texts[i]
        # Для текущего текста ищем соответствующую подглаву
        for subtopic in subtopics:
            # Проверяем, начинается ли текст с подглавы и новой строки или двоеточия и новой строки
            pattern = f'^{re.escape(subtopic)}(\n|:\n)'
            if re.match(pattern, text):
                # Удаляем подглаву из начала текста
                text = re.sub(pattern, '', text, count=1)
                removed_subtopics.append(subtopic)
                break  # Переходим к следующему тексту после нахождения совпадения

        # Добавляем измененный текст в список updated_texts
        updated_texts.append(text)

    return updated_texts, removed_subtopics

def extract_bibliography(bibliography_text):
    """
        Функция extract_bibliography редактирует текст списка литературы, удаляя нумерацию и лишние тексты от чата.

        Принимает:
        - bibliography_text (str): исходный текст списка литературы.

        Возвращает:
        - result_text (str): отредактированный текст списка литературы.
    """

    # Разделение текста на строки
    lines = bibliography_text.split('\n')

    # Создание списка для хранения строк с нумерацией
    bibliography_lines = []

    # Проходимся по каждой строке и проверяем, начинается ли она с нумерации
    for line in lines:
        if re.match(r'^\d+\.\s', line):
            # Удаляем нумерацию из строки
            line_without_numbering = re.sub(r'^\d+\.\s', '', line)
            bibliography_lines.append(line_without_numbering)

    # Соединяем строки обратно в текст с сохранением переносов строк
    result_text = '\n'.join(bibliography_lines)
    return result_text

def remove_asterisks(text_list):
    """
        Функция remove_asterisks удаляет символы '**' и '#' из текстов.

        Принимает:
        - text_list (list): массив текстов подтем.

        Возвращает:
        - updated_texts (list): массив обновленных текстов без символов '**' и '#'.
    """

    # Создаем список для хранения измененных текстов
    updated_texts = []

    # Проходимся по каждому элементу списка
    for text in text_list:
        # Удаляем все вхождения "**"
        updated_text = text.replace("**", "")
        new_updated_text = updated_text.replace("#", "")
        # Добавляем измененный текст в список updated_texts
        updated_texts.append(new_updated_text)

    return updated_texts






