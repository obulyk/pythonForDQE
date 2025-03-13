import  re
def normalize_text(text):
    # Capitalize the first letter of the whole text
    text = text.strip().capitalize()

    # Fix the misspelling "iz" to "is"
    text = re.sub(r'\biz\b', 'is', text)

    # Normalize letter case by making the first letter of each sentence uppercase
    sentences = re.split(r'([.?!:])', text)
    sentences = [s.strip().capitalize() for s in sentences if s]

    # Join sentences back together
    text = ''.join(sentences)

    # Create a new sentence with the last words of each sentence
    last_words = [s.strip().split()[-1] for s in sentences if s]
    new_sentence = " ".join(last_words) + "."

    # Add the new sentence to the end of the text
    text += " " + new_sentence

    # Count all whitespaces (spaces, newlines, tabs)
    whitespace_count = len(re.findall(r'\s', text))  # \s matches any whitespace character (spaces, tabs, newlines)

    return text, whitespace_count

# Homework text
homework_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Normalize and process the text
processed_text, whitespace_count = normalize_text(homework_text)

print("Processed Text:\n", processed_text)
print("\nWhitespace Count:", whitespace_count)