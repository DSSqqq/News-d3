from django import template
import re

register = template.Library()

CENSORED_WORDS = ['дурак', 'редиска']

@register.filter
def censor(text):
    if not text:
        return text

    def replace_word(match):
        word = match.group(0)
        # Проверяем, что слово в списке запрещенных
        if word.lower() in CENSORED_WORDS:
            # Оставляем первую букву, заменяем остальные на *
            return word[0] + '*' * (len(word) - 1)
        return word

    # Используем регулярное выражение для поиска слов
    pattern = re.compile(r'\b\w+\b', re.IGNORECASE)
    return pattern.sub(replace_word, text)