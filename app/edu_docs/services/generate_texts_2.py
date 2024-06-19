import random
import os


def generate_texts(language_of_work, subtopics, client, context, page_count):
    """
    Генерация текста для работы с использованием API OpenAI.

    Аргументы:
    - language_of_work (str): язык работы.
    - subtopics (list): список подтем.
    - client (object): клиент для взаимодействия с ChatGPT.
    - context (list): контекст чата.
    - page_count (str): количество страниц.

    Возвращает:
    - subtopic_texts (list): список текстов для подтем.
    - context (list): обновленный контекст.
    """
    client.api_key = os.getenv('OPENAI_API_KEY')
    subtopic_texts = []

    if language_of_work == "1":  # Кыргызский
        subtopic_texts = generate_texts_kg(subtopics, client, context, page_count)
    elif language_of_work == "2":  # Русский
        subtopic_texts = generate_texts_ru(subtopics, client, context, page_count)
    elif language_of_work == "3":  # Английский
        subtopic_texts = generate_texts_en(subtopics, client, context, page_count)

    return subtopic_texts, context


def generate_texts_kg(subtopics, client, context, page_count):
    subtopic_texts = []
    if page_count == "1":
        subtopic_texts.extend([
            generate_introduction_one_page_kg(subtopics[0], client, context, subtopic_texts, page_count),
            generate_one_page_kg(subtopics[2], client, context, subtopic_texts),
            generate_one_page_kg(subtopics[3], client, context, subtopic_texts),
            generate_one_page_kg(subtopics[4], client, context, subtopic_texts),
            generate_one_page_kg(subtopics[6], client, context, subtopic_texts),
            generate_one_page_kg(subtopics[7], client, context, subtopic_texts),
            generate_one_page_kg(subtopics[8], client, context, subtopic_texts),
            generate_one_page_kg(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_kg(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "2":
        subtopic_texts.extend([
            generate_introduction_one_page_kg(subtopics[0], client, context, subtopic_texts, page_count),
            generate_two_page_kg(subtopics[2], client, context, subtopic_texts),
            generate_two_page_kg(subtopics[3], client, context, subtopic_texts),
            generate_two_page_kg(subtopics[4], client, context, subtopic_texts),
            generate_two_page_kg(subtopics[6], client, context, subtopic_texts),
            generate_two_page_kg(subtopics[7], client, context, subtopic_texts),
            generate_two_page_kg(subtopics[8], client, context, subtopic_texts),
            generate_two_page_kg(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_kg(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "3":
        subtopic_texts.extend([
            generate_introduction_one_page_kg(subtopics[0], client, context, subtopic_texts, page_count),
            generate_four_page_kg(subtopics[2], client, context, subtopic_texts),
            generate_three_page_kg(subtopics[3], client, context, subtopic_texts),
            generate_three_page_kg(subtopics[4], client, context, subtopic_texts),
            generate_four_page_kg(subtopics[6], client, context, subtopic_texts),
            generate_three_page_kg(subtopics[7], client, context, subtopic_texts),
            generate_three_page_kg(subtopics[8], client, context, subtopic_texts),
            generate_two_page_kg(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_kg(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "4":
        subtopic_texts.extend([
            generate_introduction_one_page_kg(subtopics[0], client, context, subtopic_texts, page_count),
            generate_six_page_kg(subtopics[2], client, context, subtopic_texts),
            generate_five_page_kg(subtopics[3], client, context, subtopic_texts),
            generate_five_page_kg(subtopics[4], client, context, subtopic_texts),
            generate_six_page_kg(subtopics[6], client, context, subtopic_texts),
            generate_five_page_kg(subtopics[7], client, context, subtopic_texts),
            generate_five_page_kg(subtopics[8], client, context, subtopic_texts),
            generate_three_page_kg(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_kg(client, context, subtopic_texts, page_count)
        ])
    return subtopic_texts


def generate_texts_ru(subtopics, client, context, page_count):
    subtopic_texts = []
    if page_count == "1":
        subtopic_texts.extend([
            generate_introduction_one_page_ru(subtopics[0], client, context, subtopic_texts, page_count),
            generate_one_page_ru(subtopics[2], client, context, subtopic_texts),
            generate_one_page_ru(subtopics[3], client, context, subtopic_texts),
            generate_one_page_ru(subtopics[4], client, context, subtopic_texts),
            generate_one_page_ru(subtopics[6], client, context, subtopic_texts),
            generate_one_page_ru(subtopics[7], client, context, subtopic_texts),
            generate_one_page_ru(subtopics[8], client, context, subtopic_texts),
            generate_one_page_ru(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_ru(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "2":
        subtopic_texts.extend([
            generate_introduction_one_page_ru(subtopics[0], client, context, subtopic_texts, page_count),
            generate_two_page_ru(subtopics[2], client, context, subtopic_texts),
            generate_two_page_ru(subtopics[3], client, context, subtopic_texts),
            generate_two_page_ru(subtopics[4], client, context, subtopic_texts),
            generate_two_page_ru(subtopics[6], client, context, subtopic_texts),
            generate_two_page_ru(subtopics[7], client, context, subtopic_texts),
            generate_two_page_ru(subtopics[8], client, context, subtopic_texts),
            generate_two_page_ru(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_ru(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "3":
        subtopic_texts.extend([
            generate_introduction_one_page_ru(subtopics[0], client, context, subtopic_texts, page_count),
            generate_four_page_ru(subtopics[2], client, context, subtopic_texts),
            generate_three_page_ru(subtopics[3], client, context, subtopic_texts),
            generate_three_page_ru(subtopics[4], client, context, subtopic_texts),
            generate_four_page_ru(subtopics[6], client, context, subtopic_texts),
            generate_three_page_ru(subtopics[7], client, context, subtopic_texts),
            generate_three_page_ru(subtopics[8], client, context, subtopic_texts),
            generate_two_page_ru(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_ru(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "4":
        subtopic_texts.extend([
            generate_introduction_one_page_ru(subtopics[0], client, context, subtopic_texts, page_count),
            generate_six_page_ru(subtopics[2], client, context, subtopic_texts),
            generate_five_page_ru(subtopics[3], client, context, subtopic_texts),
            generate_five_page_ru(subtopics[4], client, context, subtopic_texts),
            generate_six_page_ru(subtopics[6], client, context, subtopic_texts),
            generate_five_page_ru(subtopics[7], client, context, subtopic_texts),
            generate_five_page_ru(subtopics[8], client, context, subtopic_texts),
            generate_three_page_ru(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_ru(client, context, subtopic_texts, page_count)
        ])
    return subtopic_texts


def generate_texts_en(subtopics, client, context, page_count):
    subtopic_texts = []
    if page_count == "1":
        subtopic_texts.extend([
            generate_introduction_one_page_en(subtopics[0], client, context, subtopic_texts, page_count),
            generate_one_page_en(subtopics[2], client, context, subtopic_texts),
            generate_one_page_en(subtopics[3], client, context, subtopic_texts),
            generate_one_page_en(subtopics[4], client, context, subtopic_texts),
            generate_one_page_en(subtopics[6], client, context, subtopic_texts),
            generate_one_page_en(subtopics[7], client, context, subtopic_texts),
            generate_one_page_en(subtopics[8], client, context, subtopic_texts),
            generate_one_page_en(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_en(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "2":
        subtopic_texts.extend([
            generate_introduction_one_page_en(subtopics[0], client, context, subtopic_texts, page_count),
            generate_two_page_en(subtopics[2], client, context, subtopic_texts),
            generate_two_page_en(subtopics[3], client, context, subtopic_texts),
            generate_two_page_en(subtopics[4], client, context, subtopic_texts),
            generate_two_page_en(subtopics[6], client, context, subtopic_texts),
            generate_two_page_en(subtopics[7], client, context, subtopic_texts),
            generate_two_page_en(subtopics[8], client, context, subtopic_texts),
            generate_two_page_en(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_en(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "3":
        subtopic_texts.extend([
            generate_introduction_one_page_en(subtopics[0], client, context, subtopic_texts, page_count),
            generate_four_page_en(subtopics[2], client, context, subtopic_texts),
            generate_three_page_en(subtopics[3], client, context, subtopic_texts),
            generate_three_page_en(subtopics[4], client, context, subtopic_texts),
            generate_four_page_en(subtopics[6], client, context, subtopic_texts),
            generate_three_page_en(subtopics[7], client, context, subtopic_texts),
            generate_three_page_en(subtopics[8], client, context, subtopic_texts),
            generate_two_page_en(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_en(client, context, subtopic_texts, page_count)
        ])
    elif page_count == "4":
        subtopic_texts.extend([
            generate_introduction_one_page_en(subtopics[0], client, context, subtopic_texts, page_count),
            generate_six_page_en(subtopics[2], client, context, subtopic_texts),
            generate_five_page_en(subtopics[3], client, context, subtopic_texts),
            generate_five_page_en(subtopics[4], client, context, subtopic_texts),
            generate_six_page_en(subtopics[6], client, context, subtopic_texts),
            generate_five_page_en(subtopics[7], client, context, subtopic_texts),
            generate_five_page_en(subtopics[8], client, context, subtopic_texts),
            generate_three_page_en(subtopics[9], client, context, subtopic_texts),
            generate_a_bibliography_en(client, context, subtopic_texts, page_count)
        ])
    return subtopic_texts


# _________________________Кыргызский язык_____________________________________

# Генерация введение (кыргызский)
def generate_introduction_one_page_kg(one_subtopic, client, context, subtopic_texts, page_count):
    """
    Генерирует текст введения на кыргызском языке с помощью API OpenAI и добавляет его в subtopic_texts.

    Аргументы:
    - one_subtopic (str): подглава или глава.
    - client (object): клиентский объект для взаимодействия с ChatGPT.
    - context (list): массив контекста чата.
    - subtopic_texts (list): массив текстов для подтем.
    - page_count (str): количество страниц.

    Возвращает:
    - subtopic_texts (list): обновленный массив текстов для подтем.
    """
    prompt_subtopic = (
        f"Информативдүү, узун текст түзүңүз, ал толугу менен '{one_subtopic}' подтемасына арналсын. "
        "Эске алыңыз, бул тексттин бащында эч кандай подглавалардын аталыштары көрсөтүлбөшү керек. "
        "Берилген подтемага тиешелүү мазмунга гана көңүл буруңуз. Текст теманын актуалдуулугун, изилдөөнүн максаттары "
        "жана милдеттерин камтышы керек."
    )

    max_tokens_dict = {
        "1": 450,
        "2": 850,
        "3": 850,
        "4": 850
    }

    # Формируем запрос на генерацию текста по указанной подтеме
    context.append({"role": "user", "content": prompt_subtopic})
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,
        max_tokens=max_tokens_dict[page_count]
    )
    subtopic_text = subtopic_completion.choices[0].message.content
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))
    sentences = subtopic_text.split('.')

    if len(sentences) > 1:
        subtopic_text = '.'.join(sentences[:-1]) + '.'
    else:
        subtopic_text = ''

    if page_count == "4":
        paragraphs = subtopic_text.strip().split('\n')
        last_paragraph = paragraphs[-1]
        prompt_subtopic = (
            f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
            f"\"{last_paragraph}\"\n\n"
            "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, "
            "көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз. Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
        )
        context.append({"role": "user", "content": prompt_subtopic})
        subtopic_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=context,
            temperature=0.8,
            max_tokens=450
        )
        subtopic_text_last = subtopic_completion.choices[0].message.content
        subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))
        sentences = subtopic_text_last.split('.')

        if len(sentences) > 1:
            subtopic_text_last = '.'.join(sentences[:-1]) + '.'
        else:
            subtopic_text_last = ''

        subtopic_text = subtopic_text + "\n" + subtopic_text_last
        context.pop()

    subtopic_texts.append(subtopic_text)
    print(subtopic_text + "\n\n")
    context.pop()
    return subtopic_texts


# Генерация 1 страницу (кыргызский)
def generate_one_page_kg(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_one_page_kg генерирует одну страницу текста на кыргызском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Информативдүү, аябай узун текст түзүңүз, ал толугу менен '{one_subtopic}' темасына арналсын. Эске алыңыз, бул тексттин бащында эч кандай подглавалардын аталыштары көрсөтүлбөшү керек. Берилген подтемага тиешелүү мазмунга гана көңүл буруңуз."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=450  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text = '.'.join(sentences[:-1]) + '.'

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем редактированный текст для отображения
    print(subtopic_text + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts

# Генерация 2 страницу (кыргызский)
def generate_two_page_kg(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_two_page_kg генерирует две страницы текста на кыргызском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Информативдүү, аябай узун текст түзүңүз, ал толугу менен '{one_subtopic}' темасына арналсын. Эске алыңыз, бул тексттин бащында эч кандай подглавалардын аталыштары көрсөтүлбөшү керек. Берилген подтемага тиешелүү мазмунга гана көңүл буруңуз."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text = '.'.join(sentences[:-1]) + '.'

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем редактированный текст для отображения
    print(subtopic_text + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts

# Генерация 3 страницу (кыргызский)
def generate_three_page_kg(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_three_page_kg генерирует три страницы текста на кыргызском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """
    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Информативдүү, аябай узун текст түзүңүз, ал толугу менен '{one_subtopic}' темасына арналсын. Эске алыңыз, бул тексттин бащында эч кандай подглавалардын аталыштары көрсөтүлбөшү керек. Берилген подтемага тиешелүү мазмунга гана көңүл буруңуз."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
        f"\"{last_paragraph}\"\n\n"
        "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз."
        "Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=450  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 4 страницу (кыргызский)
def generate_four_page_kg(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_four_page_kg генерирует четыре страницы текста на кыргызском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Информативдүү, аябай узун текст түзүңүз, ал толугу менен '{one_subtopic}' темасына арналсын. Эске алыңыз, бул тексттин бащында эч кандай подглавалардын аталыштары көрсөтүлбөшү керек. Берилген подтемага тиешелүү мазмунга гана көңүл буруңуз."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
        f"\"{last_paragraph}\"\n\n"
        "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз."
        "Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 5 страницу (кыргызский)
def generate_five_page_kg(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_five_page_kg генерирует пять страниц текста на кыргызском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """
    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Информативдүү, аябай узун текст түзүңүз, ал толугу менен '{one_subtopic}' темасына арналсын. Эске алыңыз, бул тексттин бащында эч кандай подглавалардын аталыштары көрсөтүлбөшү керек. Берилген подтемага тиешелүү мазмунга гана көңүл буруңуз."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
        f"\"{last_paragraph}\"\n\n"
        "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз."
        "Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_second = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_second = '\n'.join(subtopic_text_second.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_second.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_second = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_second = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_second.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
        f"\"{last_paragraph}\"\n\n"
        "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз."
        "Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=450  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_second + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 6 страницу (кыргызский)
def generate_six_page_kg(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_six_page_kg генерирует шесть страниц текста на кыргызском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """
    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Информативдүү, аябай узун текст түзүңүз, ал толугу менен '{one_subtopic}' темасына арналсын. Эске алыңыз, бул тексттин бащында эч кандай подглавалардын аталыштары көрсөтүлбөшү керек. Берилген подтемага тиешелүү мазмунга гана көңүл буруңуз."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # Печатаем редактированный текст для отображения
    print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
        f"\"{last_paragraph}\"\n\n"
        "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз."
        "Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_second = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_second = '\n'.join(subtopic_text_second.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    print(subtopic_text_second + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_second.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_second = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_second = '.'.join(sentences[:-1]) + '.'

    # Печатаем редактированный текст для отображения
    print(subtopic_text_second + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_second.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
        f"\"{last_paragraph}\"\n\n"
        "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз."
        "Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=850  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # Печатаем редактированный текст для отображения
    print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_last.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Сиз '{one_subtopic}' темасында текст жазып бүттүңүз жана аны төмөнкүдөй аяктадыңыз:\n"
        f"\"{last_paragraph}\"\n\n"
        "Текстти кайталоосуз улантып, узунураак жана деталдаштырылган сүрөттөмө кошуңуз. Теманы тереңирээк ачып бериңиз, көбүрөөк маалымат жана деталдарды кошуп, текстти бай жана информативдүү кылып жазыңыз."
        "Эч кандай өзүңдүн сөзүңүздү кошпоңуз!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=400  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last_last = '\n'.join(subtopic_text_last_last.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    print(subtopic_text_last_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last_last = '.'.join(sentences[:-1]) + '.'

    # Печатаем редактированный текст для отображения
    print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_second + "\n" + subtopic_text_last + "\n" + subtopic_text_last_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация список литературы (русский)
def generate_a_bibliography_kg(client, context, subtopic_texts, page_count):
    """
        Функция generate_a_bibliography_kg генерирует список литературы на кыргызском языке
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Генерация случайного числа от 5 до 10 включительно
    random_number = ""
    if page_count == "1":
        random_number = random.randint(5, 10)
    elif page_count == "2":
        random_number = random.randint(7, 10)
    elif page_count == "3":
        random_number = random.randint(10, 15)
    elif page_count == "4":
        random_number = random.randint(13, 15)

    # Формируем запрос на генерацию списка литературы
    prompt_subtopic = f"Кыргыз тилинде {random_number} штук 'колдонулган адабияттардын тизмесин' жазыңыз."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7  # Контролируем креативность и разнообразие ответов
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content

    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    print(subtopic_text + "\n\n")

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts


# _________________________Русский язык_____________________________________

# Генерация введение (русский)
def generate_introduction_one_page_ru(one_subtopic, client, context, subtopic_texts, page_count):
    """
        Функция generate_introduction_one_page_ru генерирует текста для введение на русском языке
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """
    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Сформулируйте информативный очень длинный текст, полностью посвящённый подтеме '{one_subtopic}'. Обратите внимание, что необходимо избежать упоминания заголовков и подзаголовков. Сосредоточьтесь исключительно на содержании, относящемся к указанной подтеме. Текст должен охватывать актуальность темы, цели и задачи исследования"

    if page_count == "1":
        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-3.5
        subtopic_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=context,
            temperature=0.7,  # Контролируем креативность и разнообразие ответов
            max_tokens=600  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text = '.'.join(sentences[:-1]) + '.'

        # Добавляем сгенерированный текст под темы в список subtopic_texts
        subtopic_texts.append(subtopic_text)

        # Печатаем редактированный текст для отображения
        print(subtopic_text + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

    elif page_count == "2" or page_count == "3":
        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-4o
        subtopic_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=context,
            temperature=0.7,  # Контролируем креативность и разнообразие ответов
            max_tokens=700  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text = '.'.join(sentences[:-1]) + '.'

        # Добавляем сгенерированный текст под темы в список subtopic_texts
        subtopic_texts.append(subtopic_text)

        # Печатаем редактированный текст для отображения
        print(subtopic_text + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

    elif page_count == "4":
        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-4o
        subtopic_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=context,
            temperature=0.7,  # Контролируем креативность и разнообразие ответов
            max_tokens=700  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text_first = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text_first + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text_first.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text_first = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text_first = '.'.join(sentences[:-1]) + '.'

        # # Печатаем редактированный текст для отображения
        # print(subtopic_text_first + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

        # Разделяем текст на абзацы по двойным переносам строк
        paragraphs = subtopic_text_first.strip().split('\n')

        # Получаем последний абзац
        last_paragraph = paragraphs[-1]

        # Формируем запрос на продолжение текста
        prompt_subtopic = (
            f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
            f"\"{last_paragraph}\"\n\n"
            "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
            "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        )

        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-3.5
        subtopic_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=context,
            temperature=0.8,  # Контролируем креативность и разнообразие ответов
            max_tokens=400  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text_last = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text_last + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text_last.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text_last = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text_last = '.'.join(sentences[:-1]) + '.'

        # # Печатаем редактированный текст для отображения
        # print(subtopic_text_last + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

        subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

        # Добавляем сгенерированный текст под темы в список subtopic_texts
        subtopic_texts.append(subtopic_text)

        # Печатаем итоговый текст для отображения
        print(subtopic_text)

    return subtopic_texts

# Генерация 1 страницу (русский)
def generate_one_page_ru(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_one_page_ru генерирует одну страницу текста на русском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Сформулируйте информативный очень длинный текст, полностью посвящённый теме '{one_subtopic}'. Обратите внимание, что необходимо избежать упоминания заголовков и подзаголовков. Сосредоточьтесь исключительно на содержании, относящемся к указанной подтеме."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text = '.'.join(sentences[:-1]) + '.'

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем редактированный текст для отображения
    print(subtopic_text + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts

# Генерация 2 страницу (русский)
def generate_two_page_ru(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_two_page_ru генерирует две страницы текста на русском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Сформулируйте информативный очень длинный текст, полностью посвящённый теме '{one_subtopic}'. Обратите внимание, что необходимо избежать упоминания заголовков и подзаголовков. Сосредоточьтесь исключительно на содержании, относящемся к указанной подтеме."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text = '.'.join(sentences[:-1]) + '.'

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем редактированный текст для отображения
    print(subtopic_text + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts

# Генерация 3 страницу (русский)
def generate_three_page_ru(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_three_page_ru генерирует три страницы текста на русском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Сформулируйте информативный очень длинный текст, полностью посвящённый теме '{one_subtopic}'. Обратите внимание, что необходимо избежать упоминания заголовков и подзаголовков. Сосредоточьтесь исключительно на содержании, относящемся к указанной подтеме."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=700  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
        f"\"{last_paragraph}\"\n\n"
        "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
        "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        "Не добавляйте никаких своих слов!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 4 страницу (русский)
def generate_four_page_ru(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_four_page_ru генерирует четыре страницы текста на русском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Сформулируйте информативный очень длинный текст, полностью посвящённый теме '{one_subtopic}'. Обратите внимание, что необходимо избежать упоминания заголовков и подзаголовков. Сосредоточьтесь исключительно на содержании, относящемся к указанной подтеме."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=700  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
        f"\"{last_paragraph}\"\n\n"
        "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
        "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        "Не добавляйте никаких своих слов!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 5 страницу (русский)
def generate_five_page_ru(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_five_page_ru генерирует пять страниц текста на русском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Сформулируйте информативный очень длинный текст, полностью посвящённый теме '{one_subtopic}'. Обратите внимание, что необходимо избежать упоминания заголовков и подзаголовков. Сосредоточьтесь исключительно на содержании, относящемся к указанной подтеме."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=700  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
        f"\"{last_paragraph}\"\n\n"
        "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
        "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        "Не добавляйте никаких своих слов!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_second = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_second = '\n'.join(subtopic_text_second.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_second.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_second = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_second = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_second.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
        f"\"{last_paragraph}\"\n\n"
        "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
        "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        "Не добавляйте никаких своих слов!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_second + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 6 страницу (русский)
def generate_six_page_ru(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_six_page_ru генерирует шесть страниц текста на русском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Сформулируйте информативный очень длинный текст, полностью посвящённый теме '{one_subtopic}'. Обратите внимание, что необходимо избежать упоминания заголовков и подзаголовков. Сосредоточьтесь исключительно на содержании, относящемся к указанной подтеме."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=700  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
        f"\"{last_paragraph}\"\n\n"
        "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
        "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        "Не добавляйте никаких своих слов!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_second = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_second = '\n'.join(subtopic_text_second.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_second.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_second = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_second = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_second.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
        f"\"{last_paragraph}\"\n\n"
        "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
        "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        "Не добавляйте никаких своих слов!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_last.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"Ты написал текст на под тему '{one_subtopic}' и закончил так:\n"
        f"\"{last_paragraph}\"\n\n"
        "Продолжай этот текст не повторяя, добавив более длинное и детализированное описание. "
        "Раскрой тему более глубоко, добавь больше информации и деталей, чтобы сделать текст более насыщенным и информативным."
        "Не добавляйте никаких своих слов!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=400  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last_last = '\n'.join(subtopic_text_last_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_second + "\n" + subtopic_text_last + "\n" + subtopic_text_last_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация список литературы (русский)
def generate_a_bibliography_ru(client, context, subtopic_texts, page_count):
    """
        Функция generate_a_bibliography_ru генерирует список литературы на русском языке
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Генерация случайного числа от 5 до 10 включительно
    random_number = ""
    if page_count == "1":
        random_number = random.randint(5, 10)
    elif page_count == "2":
        random_number = random.randint(7, 10)
    elif page_count == "3":
        random_number = random.randint(10, 15)
    elif page_count == "4":
        random_number = random.randint(13, 15)

    # Формируем запрос на генерацию списка литературы
    prompt_subtopic = f"Напиши {random_number} штук 'список литературы' на русском языке."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7  # Контролируем креативность и разнообразие ответов
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content

    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    print(subtopic_text + "\n\n")

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts


# _________________________Английский язык_____________________________________

# Генерация введение (английский)
def generate_introduction_one_page_en(one_subtopic, client, context, subtopic_texts, page_count):
    """
        Функция generate_introduction_one_page_en генерирует текста для введение на английском языке
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Formulate an informative, very long text entirely dedicated to the subtopic '{one_subtopic}'. Please note that mention of headings and subheadings should be avoided. Focus solely on content related to the specified subtopic. The text should cover the relevance of the topic, goals and objectives of the study"

    if page_count == "1":
        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-3.5
        subtopic_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=context,
            temperature=0.7,  # Контролируем креативность и разнообразие ответов
            max_tokens=280  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text = '.'.join(sentences[:-1]) + '.'

        # Добавляем сгенерированный текст под темы в список subtopic_texts
        subtopic_texts.append(subtopic_text)

        # Печатаем редактированный текст для отображения
        print(subtopic_text + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

    elif page_count == "2" or page_count == "3":
        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-4o
        subtopic_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=context,
            temperature=0.7,  # Контролируем креативность и разнообразие ответов
            max_tokens=600  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text = '.'.join(sentences[:-1]) + '.'

        # Добавляем сгенерированный текст под темы в список subtopic_texts
        subtopic_texts.append(subtopic_text)

        # Печатаем редактированный текст для отображения
        print(subtopic_text + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

    elif page_count == "4":
        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-4o
        subtopic_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=context,
            temperature=0.7,  # Контролируем креативность и разнообразие ответов
            max_tokens=600  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text_first = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text_first + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text_first.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text_first = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text_first = '.'.join(sentences[:-1]) + '.'

        # # Печатаем редактированный текст для отображения
        # print(subtopic_text_first + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

        # Разделяем текст на абзацы по двойным переносам строк
        paragraphs = subtopic_text_first.strip().split('\n')

        # Получаем последний абзац
        last_paragraph = paragraphs[-1]

        # Формируем запрос на продолжение текста
        prompt_subtopic = (
            f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
            "'{last_paragraph}'\n\n"
            "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
        )

        # Добавляем новый элемент в список контекста с запросом пользователя
        context.append({"role": "user", "content": prompt_subtopic})

        # Запрашиваем генерацию текста у модели GPT-3.5
        subtopic_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=context,
            temperature=0.8,  # Контролируем креативность и разнообразие ответов
            max_tokens=250  # Ограничиваем количество токенов в ответе
        )

        # Получаем сгенерированный текст из ответа модели
        subtopic_text_last = subtopic_completion.choices[0].message.content
        # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
        subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

        # # Печатаем сгенерированный текст для отображения
        # print(subtopic_text_last + "\n\n")

        # Удалить последнее незаконченное предложение, если есть
        sentences = subtopic_text_last.split('.')

        # Если в тексте нет точек, удалить весь текст
        if len(sentences) == 1:
            subtopic_text_last = ''
        else:
            # Удаляем последнее незаконченное предложение
            subtopic_text_last = '.'.join(sentences[:-1]) + '.'

        # # Печатаем редактированный текст для отображения
        # print(subtopic_text_last + "\n\n")

        # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
        context.pop()

        subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

        # Добавляем сгенерированный текст под темы в список subtopic_texts
        subtopic_texts.append(subtopic_text)

        # Печатаем итоговый текст для отображения
        print(subtopic_text)

    return subtopic_texts

# Генерация 1 страницу (английский)
def generate_one_page_en(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_one_page_en генерирует одну страницу текста на английском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Formulate an informative, very long text entirely dedicated to the topic '{one_subtopic}'. Please note that mention of headings and subheadings should be avoided. Focus solely on content related to the specified subtopic."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=280  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text = '.'.join(sentences[:-1]) + '.'

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем редактированный текст для отображения
    print(subtopic_text + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts

# Генерация 2 страницу (английский)
def generate_two_page_en(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_two_page_en генерирует две страницы текста на английском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Formulate an informative, very long text entirely dedicated to the topic '{one_subtopic}'. Please note that mention of headings and subheadings should be avoided. Focus solely on content related to the specified subtopic."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text = '.'.join(sentences[:-1]) + '.'

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем редактированный текст для отображения
    print(subtopic_text + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts

# Генерация 3 страницу (английский)
def generate_three_page_en(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_three_page_en генерирует три страницы текста на английском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Formulate an informative, very long text entirely dedicated to the topic '{one_subtopic}'. Please note that mention of headings and subheadings should be avoided. Focus solely on content related to the specified subtopic."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
        "'{last_paragraph}'\n\n"
        "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=360  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 4 страницу (английский)
def generate_four_page_en(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_four_page_en генерирует четыре страницы текста на английском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Formulate an informative, very long text entirely dedicated to the topic '{one_subtopic}'. Please note that mention of headings and subheadings should be avoided. Focus solely on content related to the specified subtopic."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
        "'{last_paragraph}'\n\n"
        "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 5 страницу (английский)
def generate_five_page_en(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_five_page_en генерирует пять страниц текста на английском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Formulate an informative, very long text entirely dedicated to the topic '{one_subtopic}'. Please note that mention of headings and subheadings should be avoided. Focus solely on content related to the specified subtopic."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
        "'{last_paragraph}'\n\n"
        "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_second = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_second = '\n'.join(subtopic_text_second.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_second.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_second = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_second = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_second.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
        "'{last_paragraph}'\n\n"
        "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=280  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_second + "\n" + subtopic_text_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация 6 страницу (английский)
def generate_six_page_en(one_subtopic, client, context, subtopic_texts):
    """
        Функция generate_six_page_en генерирует шесть страниц текста на английском языке для одного подглавы или главы
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Формируем запрос на генерацию текста по указанной подтеме
    prompt_subtopic = f"Formulate an informative, very long text entirely dedicated to the topic '{one_subtopic}'. Please note that mention of headings and subheadings should be avoided. Focus solely on content related to the specified subtopic."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_first = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_first = '\n'.join(subtopic_text_first.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_first.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_first = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_first = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_first + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_first.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
        "'{last_paragraph}'\n\n"
        "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.8,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_second = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_second = '\n'.join(subtopic_text_second.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_second.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_second = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_second = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_second + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_second.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
        "'{last_paragraph}'\n\n"
        "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=600  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last = '\n'.join(subtopic_text_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    # Разделяем текст на абзацы по двойным переносам строк
    paragraphs = subtopic_text_last.strip().split('\n')

    # Получаем последний абзац
    last_paragraph = paragraphs[-1]

    # Формируем запрос на продолжение текста
    prompt_subtopic = (
        f"You have written a text on the subtopic '{one_subtopic}' and ended with:\n"
        "'{last_paragraph}'\n\n"
        "Continue this text without repeating yourself, adding a longer and more detailed description. Explore the topic in depth, give more information and details to make the text richer and more informative. Please note that you must avoid mentioning headings and subheadings and do not add any of your own words!"
    )

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-4o
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.9,  # Контролируем креативность и разнообразие ответов
        max_tokens=100  # Ограничиваем количество токенов в ответе
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text_last_last = subtopic_completion.choices[0].message.content
    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text_last_last = '\n'.join(subtopic_text_last_last.split('\n\n'))

    # # Печатаем сгенерированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удалить последнее незаконченное предложение, если есть
    sentences = subtopic_text_last_last.split('.')

    # Если в тексте нет точек, удалить весь текст
    if len(sentences) == 1:
        subtopic_text_last_last = ''
    else:
        # Удаляем последнее незаконченное предложение
        subtopic_text_last_last = '.'.join(sentences[:-1]) + '.'

    # # Печатаем редактированный текст для отображения
    # print(subtopic_text_last + "\n\n")

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    subtopic_text = subtopic_text_first + "\n" + subtopic_text_second + "\n" + subtopic_text_last + "\n" + subtopic_text_last_last

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Печатаем итоговый текст для отображения
    print(subtopic_text)

    return subtopic_texts

# Генерация список литературы (английский)
def generate_a_bibliography_en(client, context, subtopic_texts, page_count):
    """
        Функция generate_a_bibliography_en генерирует список литературы на английском языке
        с помощью API OpenAI и добавляет ее в subtopic_texts.

        Принимает:
        - one_subtopic (str): один подглава или глава.
        - client (object): клиентский объект для взаимодействия с ChatGPT.
        - context (list): массив контекста чата.
        - subtopic_texts (list): массив текстов для подтем.
        - page_count (str): количество страниц.

        Возвращает:
        - subtopic_texts (list): обновленный массив текстов для подтем.
    """

    # Генерация случайного числа от 5 до 10 включительно
    random_number = ""
    if page_count == "1":
        random_number = random.randint(5, 10)
    elif page_count == "2":
        random_number = random.randint(7, 10)
    elif page_count == "3":
        random_number = random.randint(10, 15)
    elif page_count == "4":
        random_number = random.randint(13, 15)

    # Формируем запрос на генерацию списка литературы
    prompt_subtopic = f"Write {random_number} pieces 'bibliography' in English."

    # Добавляем новый элемент в список контекста с запросом пользователя
    context.append({"role": "user", "content": prompt_subtopic})

    # Запрашиваем генерацию текста у модели GPT-3.5
    subtopic_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0.7  # Контролируем креативность и разнообразие ответов
    )

    # Получаем сгенерированный текст из ответа модели
    subtopic_text = subtopic_completion.choices[0].message.content

    # Удаляем лишние пустые строки, разделяя абзацы одной новой строкой
    subtopic_text = '\n'.join(subtopic_text.split('\n\n'))

    # Печатаем сгенерированный текст для отображения
    print(subtopic_text + "\n\n")

    # Добавляем сгенерированный текст под темы в список subtopic_texts
    subtopic_texts.append(subtopic_text)

    # Удаляем последний элемент из списка контекста, чтобы сохранить оригинальный контекст
    context.pop()

    return subtopic_texts

