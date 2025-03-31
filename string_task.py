import re
import string
homework_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

paragraph = [sentence.strip().capitalize()
             for sentence in homework_text.split(b"\xc2\xa0".decode("utf-8"))]
normalized_text = '\n'.join(paragraph)

normalized_text = re.sub(r'(^|(?<=\.\s))([a-z])',
                         lambda m: m.group(1) + m.group(2).upper(),
                         normalized_text)

last_words = re.findall(r'(\b\w+\b)[.?!:]', normalized_text)

new_sentence = " ".join(last_words) + "."
text = re.sub(r'(paragraph.)', r'\1 ' + new_sentence, normalized_text)

normalized_text = re.sub(r'(?<!Fix“)iz(?!”)', 'is', text)

whitespace = len([i for i in normalized_text if i in string.whitespace])
#whitespace_count = len(re.findall(r'[\s\xa0]', normalized_text))
print(normalized_text, '\n', whitespace)
