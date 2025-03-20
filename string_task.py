import re

text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
paragraph = [sentence.strip().capitalize() for sentence in text.split('  ')]
normalized_text = '. '.join(paragraph)

normalized_text = re.sub(r'(\n\s*)', '\n', normalized_text)


print(paragraph[2].capitalize())
# # 1. Нормалізація: Перша літера кожного речення велика
# normalized_text = '. '.join([sentence.strip().capitalize() for sentence in homework_text.split('. ')])
# normalized_text = re.sub(r'(\n\s*)', '\n', normalized_text)  # Відновлюємо нові рядки
#
# # 2. Замінити "iZ" на "is", тільки коли це помилка
# normalized_text = re.sub(r'\b(iZ)\b', 'is', normalized_text)
#
# # 3. Створити нове речення з останніх слів кожного існуючого речення
# sentences = normalized_text.split('. ')
# last_words = [sentence.split()[-1] for sentence in sentences if sentence]  # Останнє слово кожного речення
# new_sentence = ' '.join(last_words) + '.'  # Створення нового речення з останніх слів
#
# # Додаємо нове речення до кінця
# normalized_text += ' ' + new_sentence
#
# # 4. Порахувати кількість пробілів і всіх пробільних символів (whitespace)
# whitespace_count = len(re.findall(r'\s', normalized_text))
#
# # Виведення результату
# print(normalized_text)
# print(f"Total number of whitespace characters: {whitespace_count}")