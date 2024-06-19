import re


def texts_editor(subtopic_texts, subtopics):
    """
    Редактирует тексты подтем.

    - Удаляет дубликаты предложений.
    - Удаляет незавершенные предложения.
    - Удаляет подглавы и главы, если они находятся в начале текста.
    - Редактирует список литературы.
    - Удаляет определенные символы ("**", "#").
    """
    new_subtopic_texts = subtopic_texts.copy()

    for i, text in enumerate(new_subtopic_texts[:8]):
        text = remove_duplicate_sentences(text)
        text = remove_incomplete_last_sentences(text)
        text = remove_subtopic_headers(subtopics, text)
        new_subtopic_texts[i] = text

    new_subtopic_texts[8] = extract_bibliography(new_subtopic_texts[8])

    new_subtopic_texts = [remove_asterisks(text) for text in new_subtopic_texts]

    for text in new_subtopic_texts:
        print(text + "\n\n")

    return new_subtopic_texts


def split_into_sentences(text):
    """
    Разделяет текст на предложения.
    """
    sentence_endings = re.compile(r'(?<=[.!?]) +')
    return sentence_endings.split(text)


def remove_duplicate_sentences(text):
    """
    Удаляет дубликаты предложений из текста.
    """
    paragraphs = text.split('\n')
    seen_sentences = set()
    unique_sentences = []
    duplicate_sentences = []

    for paragraph in paragraphs:
        sentences = split_into_sentences(paragraph)
        for sentence in sentences:
            if re.match(r'^\d+\.\s', sentence) or len(sentence) <= 5:
                unique_sentences.append(sentence)
            elif sentence not in seen_sentences:
                seen_sentences.add(sentence)
                unique_sentences.append(sentence)
            else:
                duplicate_sentences.append(sentence)

    result_text = '\n'.join(' '.join(unique_sentences[i:i+len(split_into_sentences(paragraph))]) for i, paragraph in enumerate(paragraphs))
    return result_text


def remove_incomplete_last_sentences(text):
    """
    Удаляет незавершенные предложения из текста.
    """
    paragraphs = text.split('\n')
    result_paragraphs = []

    for paragraph in paragraphs:
        sentences = split_into_sentences(paragraph)
        if sentences and not re.search(r'[.!?:]$', sentences[-1].strip()):
            sentences = sentences[:-1]
        result_paragraphs.append(' '.join(sentences))

    return '\n'.join(result_paragraphs)


def remove_subtopic_headers(subtopics, text):
    """
    Удаляет подглавы и главы из начала текста.
    """
    for subtopic in subtopics:
        pattern = f'^{re.escape(subtopic)}(\n|:\n)'
        if re.match(pattern, text):
            text = re.sub(pattern, '', text, count=1)
            break
    return text


def extract_bibliography(bibliography_text):
    """
    Редактирует текст списка литературы, удаляя нумерацию.
    """
    lines = bibliography_text.split('\n')
    bibliography_lines = [re.sub(r'^\d+\.\s', '', line) for line in lines if re.match(r'^\d+\.\s', line)]
    return '\n'.join(bibliography_lines)


def remove_asterisks(text):
    """
    Удаляет символы '**' и '#' из текста.
    """
    return text.replace("**", "").replace("#", "")
