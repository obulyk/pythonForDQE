import re

homework_text = """homEwork:
    tHis iz your homeWork, copy these Text to variable.

    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def norm_text(homework_text):
    paragraph = [sentence.strip().capitalize()
                 for sentence in homework_text.split(' ' and '\n')]
    normalized_text = '\n'.join(paragraph)
    normalized_text = re.sub(r'(^|(?<=\.\s))([a-z])',
                             lambda m: m.group(1) + m.group(2).upper(),
                             normalized_text)
    return normalized_text

def last_words(normalized_text):
    last_words = re.findall(r'(\b\w+\b)[.?!:]', normalized_text)
    return " ".join(last_words) + "."

def fix_misspelling(text):
    return re.sub(r' iz ', ' is ', text)

def count_whitespaces(normalized_text):
    return len(re.findall(r'\s+', normalized_text))

def homework(homework_text):
    normalized_text = norm_text(homework_text)
    last_words_sentence = last_words(normalized_text)
    text_with_last_words = re.sub(r'(paragraph.)', r'\1 '
                                  + last_words_sentence, normalized_text)
    corrected_text = fix_misspelling(text_with_last_words)
    whitespace_count = count_whitespaces(corrected_text)

    return corrected_text, whitespace_count

normalized_text, whitespace_count = homework(homework_text)
print(normalized_text, '\nWhitespace count:', whitespace_count)
