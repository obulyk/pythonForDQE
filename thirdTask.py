import re

from robot.utils import normalize

global text
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

countWhiteSpaces = 0
global stringSentence

def letterLowerCases(text):
    global textLower
    textLower = text.lower().replace('','').replace('\n','')
    textLower = text.strip('\n\xa0 ').capitalize()
    sentences = re.split(r'([.?!])', textLower)
    sentences = [textLower for s in sentences]

    #sentances = re.split(r'([.?:,])', textLower)
    #textLower = re.sub(r'\s([:,.])', r'\1', textLower)
   # normalized_sentance = [s.capitalize() for s in sentances]
    #textLower = ''.join(sentences)
    return sentences
print(letterLowerCases(text))
"""
def lastWordsSentence(text):
    letterLowerCases(text)
    import re
    sentence = ""
    stringSentence = ""
    wordsWithDots = re.findall(r'\w+\.', textLower)
    for ele in wordsWithDots:
        stringSentence += ele + ' '
        sentence = stringSentence.lower().replace('.', '')
    oneStr = textLower.format(sentence)
    return oneStr

print(lastWordsSentence(text))
def missSpellingFixedText(func):
    letterLowerCases(text)
    for words in textLower:
        ch_text = re.sub(r'\biz\b', 'is', textLower)
    return (ch_text.replace('{}', ''))

print(missSpellingFixedText(text))

def findAllWhiteSpaces(t):
    print(missSpellingFixedText(t))
    t.lower()
    whiteSpaces = re.findall(r'\s', t)
    return print(whiteSpaces.__len__())


findAllWhiteSpaces(text)"""