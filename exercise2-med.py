import re

def count_words(text):
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)
    dict = {}

    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    return dict

text = input()
print(count_words(text))