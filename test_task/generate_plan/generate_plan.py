import os


def generate_plan(client):
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
    # Количества страниц
    page_counts = {
        "1": "1-10",
        "2": "10-20",
        "3": "20-30",
        "4": "30-40"
    }

    chatbot_response = ""
    work_theme = ""
    work_type = ""
    university = ""
    author_name = ""
    group_name = ""
    teacher_name = ""
    language_of_work = ""
    page_count = ""
    cover_page_data = ""

    # Попросим выбрать язык для общения
    language_of_talk = input("\033[1mСүйлөшүү тилин тандаңыз:\nВыберите язык для общения:\nChoose a language to communicate:\033[0m\n\033[94m\n1️⃣ Кыргызча\n2️⃣ Русский\n3️⃣ English\033[0m\n⚠️ Напишите соответсвующую цифру: ")
    # Если выбрано русский язык
    if language_of_talk == "2":
        print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Попросим выбрать тип работы
        work_type = input("\033[1m Выберите тип работы: \033[0m\n\033[94m1️⃣ Реферат\n2️⃣ СРС\n3️⃣ Курсовая работа\n4️⃣ Доклад\033[0m\n⚠️ Напишите соответсвующую цифру: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Попросим выбрать язык работы
        language_of_work = input("\033[1m Выберите язык работы:\033[0m\n\033[94m\n1️⃣ Кыргызча\n2️⃣ Русский\n3️⃣ English\033[0m\n⚠️ Напишите соответсвующую цифру: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Попросим выбрать тему работы
        work_theme = input("\033[1m Напишите тему работы: \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Попросим выбрать предмет работы
        discipline = input("\033[1m Напишите дисциплину(предмет): \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Попросим выбрать количество страниы работы
        page_count = input("\033[1m Выберите количество страниц:\033[0m\n\033[94m\n1️⃣ 10-15 стр\n2️⃣ 15-20 стр\n3️⃣ 20-25 стр\n4️⃣ 25-30 стр\033[0m\n⚠️ Напишите соответсвующую цифру: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Попросим написать пожелания к теме, если они есть
        wishes = input("\033[1m Напишите пожелания к теме, если они есть: \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Попросим, нужен ли титульный лист
        cover_page_data = input("\033[1m Нужен ли титульный лист:\033[0m\n\033[94m\n1️⃣ Да\n2️⃣ Нет\n3️⃣ Пустой титульный лист\033[0m\n⚠️ Напишите соответсвующую цифру: ")
        # Если нужен
        if cover_page_data == "1":  # Титульный лист добавить
            # Попросим написать название университета
            university = input("\033[1m Напишите название университета: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            # Попросим написать ФИО исполнителя
            author_name = input("\033[1m Напишите ФИО исполнителя работы: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            # Попросим написать группы исполнителя
            group_name = input("\033[1m Напишите группу выполнителя работ: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            # Попросим написать ФИО преподавателя
            teacher_name = input("\033[1m Напишите ФИО преподавателя: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        # Добавить пустой титульный лист
        elif cover_page_data == "3":
            university = " "
            author_name = "___________________________"
            group_name = "___________________________"
            teacher_name = "___________________________"

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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            # print(f"Plan for the {work_type} on the topic '{work_theme}':")
            for chunk in stream:
                # Получение текстового ответа
                response = chunk.choices[0].delta.content
                # print(response, end="")
                if response:
                    chatbot_response += response

            context = prompt + [{"role": "assistant", "content": chatbot_response}]
    # Если выбрано кыргызский язык
    elif language_of_talk == "1":
        print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        work_type = input(
            "\033[1m Иштин тибин тандаңыз: \033[0m\n\033[94m1️⃣ Реферат\n2️⃣ СРС\n3️⃣ Курстук иш\n4️⃣ Доклад\033[0m\n⚠️ Туура келген санды тандаңыз: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        language_of_work = input(
            "\033[1m Иштин тилин тандаңыз:\033[0m\n\033[94m\n1️⃣ Кыргызча\n2️⃣ Русский\n3️⃣ English\033[0m\n⚠️ Туура келген санды тандаңыз: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        work_theme = input("\033[1m Иштин темасын жазыңыз: \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        discipline = input("\033[1m Дисциплинанын аталышын жазыңыз(предмет): \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        page_count = input(
            "\033[1m Канча барак болуусу керек:\033[0m\n\033[94m\n1️⃣ 10-15 стр\n2️⃣ 15-20 стр\n3️⃣ 20-25 стр\n4️⃣ 25-30 стр\033[0m\n⚠️ Туура келген санды тандаңыз: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        wishes = input("\033[1m Темага кошумча маалымат жазыңыз: \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        cover_page_data = input(
            "\033[1m Титулдук барак кошуш керекпи:\033[0m\n\033[94m\n1️⃣ Ооба\n2️⃣ Жок\n3️⃣ Бош титулдук барак кошуу\033[0m\n⚠️ Туура келген санды тандаңыз: ")
        if cover_page_data == "1":  # Титульный лист добавить
            university = input("\033[1m Университеттин атын жазңыз: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            author_name = input("\033[1m Аткаруучунун аты-жөнүн жазыңыз: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            group_name = input("\033[1m Аткаруусунун группасынын аталышын жазыңыз: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            teacher_name = input("\033[1m Текшерүүчүнүн аты-жөнүн жазыңыз: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        elif cover_page_data == "3":  # Добавить пустой титульный лист
            university = " "
            author_name = "___________________________"
            group_name = "___________________________"
            teacher_name = "___________________________"

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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            # print(f"Plan for the {work_type} on the topic '{work_theme}':")
            for chunk in stream:
                # Получение текстового ответа
                response = chunk.choices[0].delta.content
                # print(response, end="")
                if response:
                    chatbot_response += response

            context = prompt + [{"role": "assistant", "content": chatbot_response}]
    # Если выбрано английский язык
    elif language_of_talk == "3":  # Если выбрано английский язык
        print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        work_type = input(
            "\033[1m Select work type: \033[0m\n\033[94m1️⃣ Essay\n2️⃣ Student's independent work\n3️⃣ Course work\n4️⃣ Report\033[0m\n⚠️ Write the corresponding number: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        language_of_work = input(
            "\033[1m Select work language:\033[0m\n\033[94m\n1️⃣ Kyrgyz\n2️⃣ Russian\n3️⃣ English\033[0m\n⚠️ Write the corresponding number: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        work_theme = input("\033[1m Write the topic of the work: \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        discipline = input("\033[1m Write the discipline (subject): \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        page_count = input(
            "\033[1m Select number of pages:\033[0m\n\033[94m\n1️⃣ 10-15 page\n2️⃣ 15-20 page\n3️⃣ 20-25 page\n4️⃣ 25-30 page\033[0m\n⚠️ Write the corresponding number: ")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        wishes = input("\033[1m Write your wishes for the topic, if you have any: \033[0m\n")
        print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        cover_page_data = input(
            "\033[1m Is a title page necessary:\033[0m\n\033[94m\n1️⃣ Yes\n2️⃣ No\n3️⃣ Blank title page\033[0m\n⚠️ Write the corresponding number: ")
        if cover_page_data == "1":  # Титульный лист добавить
            university = input("\033[1m Write the name of the university: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            author_name = input("\033[1m Write the name of the person doing the work: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            group_name = input("\033[1m Write the name of the group: \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            teacher_name = input("\033[1m Write the teacher's name"
                                 ": \033[0m\n")
            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        elif cover_page_data == "3":  # Добавить пустой титульный лист
            university = " "
            author_name = "___________________________"
            group_name = "___________________________"
            teacher_name = "___________________________"

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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
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

            print("\n\n※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
            # print(f"Plan for the {work_type} on the topic '{work_theme}':")
            for chunk in stream:
                # Получение текстового ответа
                response = chunk.choices[0].delta.content
                # print(response, end="")
                if response:
                    chatbot_response += response

            context = prompt + [{"role": "assistant", "content": chatbot_response}]

    return chatbot_response, language_of_work, context, work_theme, university, work_type, author_name, group_name, teacher_name, page_count, cover_page_data, language_of_talk
