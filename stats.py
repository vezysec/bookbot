def count_words(text):
    number = len(text.split())
    return number

def count_each_char(text):
    letters = {}
    for char in text:
        try:
          letters[char.lower()] += 1
        except KeyError:
          letters[char.lower()] = 1  
    return letters