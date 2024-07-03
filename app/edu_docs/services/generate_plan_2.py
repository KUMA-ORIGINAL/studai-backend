import os


def generate_plan(
        client,
        language_of_work,
        work_theme,
        discipline,
        work_type,
        page_count,
        wishes,):
    """
        Функция generateplan генерирует план работы через API OpenAI.

        Принимает:
        - client (object): клиентский объект для взаимодействия с ChatGPT.

        Возвращает:
        - chatbot_response (str): ответ чат-бота.
        - language_of_work (str): язык работы.
        - context (list): контекст чата.
        - work_theme (str): тема работы.
        - university (str): название университета.
        - work_type (str): тип работы.
        - author_name (str): имя автора.
        - group_name (str): название группы.
        - teacher_name (str): имя преподавателя.
        - page_count (str): количество страниц.
        - cover_page_data (str): титульный лист (добавить/не добавить).
        - language_of_talk (str): язык общения.
    """

    context = []

    client.api_key = os.getenv('OPENAI_API_KEY')
    # Словарь для соответствия чисел текстовым описаниям типа работы и количества страниц
    # На кыргызском
    work_types_ru = {
        "1": "Реферат",
        "2": "Самостоятельная работа студента",
        "3": "Курсовая работа",
        "4": "Доклад"
    }
    # На русском
    work_types_kg = {
        "1": "Реферат",
        "2": "Студенттин өз алдынча иши",
        "3": "Курстук иш",
        "4": "Доклад"
    }
    # На английском
    work_types_en = {
        "1": "Essay",
        "2": "Student's independent work",
        "3": "Course work",
        "4": "Report"
    }

    chatbot_response = ""

    # Попросим выбрать тип работы
    work_type = work_type
    # Попросим выбрать язык работы
    language_of_work = language_of_work
    # Попросим выбрать тему работы
    work_theme = work_theme
    # Попросим выбрать предмет работы
    discipline = discipline
    # Попросим выбрать количество страниы работы
    page_count = page_count
    # Попросим написать пожелания к теме, если они есть
    wishes = wishes
    # Составить план на кыргызском
    if language_of_work == "1":
        work_type = work_types_kg.get(work_type)
        first_prompt = f"Мен '{work_theme}' деген темага {work_type} жасашым керек. Дисциплинанын аты: {discipline}. {wishes} Мага кыскача жана эффективдүү план түзүп берчи. Структуре: Киришүү, 1-Бөлүм., 1.1., 1.2, 1.3., 2-Бөлүм, 2.1., 2.2., 2.3., Корутунду, Колдонулган адабияттар"
        prompt = context + [{"role": "user", "content": first_prompt}]

        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=prompt,
            stream=True
        )

        # print(f"'{work_theme}' темасына {work_type} планы:")
        for chunk in stream:
            # Получение текстового ответа
            response = chunk.choices[0].delta.content
            # print(response, end="")
            if response:
                chatbot_response += response

        context = prompt + [{"role": "assistant", "content": chatbot_response}]

    # Составить план на русском
    if language_of_work == "2":
        work_type = work_types_ru.get(work_type)
        first_prompt = f"Мне надо написать {work_type} на тему '{work_theme}'. Название дисциплины: {discipline}. {wishes} Составь короткий и эффективный план по структуре: Введение, Глава 1., 1.1., 1.2, 1.3., Глава 2, 2.1., 2.2., 2.3., Заключение, Список литературы"
        prompt = context + [{"role": "user", "content": first_prompt}]

        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            stream=True
        )

        # print(f"План по типу работы {work_type} на тему '{work_theme}':")
        for chunk in stream:
            # Получение текстового ответа
            response = chunk.choices[0].delta.content
            # print(response, end="")
            if response:
                chatbot_response += response

        context = prompt + [{"role": "assistant", "content": chatbot_response}]

    # Составить план на английском
    if language_of_work == "3":
        work_type = work_types_en.get(work_type)
        first_prompt = f"I need to write a {work_type} on the topic '{work_theme}'. Name of discipline: {discipline}. {wishes}. Create a concise and impactful plan strictly with the following structure: Introduction, Chapter 1, 1.1, 1.2, 1.3, Chapter 2, 2.1, 2.2, 2.3, Conclusion, References."
        prompt = context + [{"role": "user", "content": first_prompt}]

        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            stream=True
        )

        # print(f"Plan for the {work_type} on the topic '{work_theme}':")
        for chunk in stream:
            # Получение текстового ответа
            response = chunk.choices[0].delta.content
            # print(response, end="")
            if response:
                chatbot_response += response

        context = prompt + [{"role": "assistant", "content": chatbot_response}]

    return chatbot_response, context
