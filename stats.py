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

def sort_letters_by_count(letters):
   chars_list = []
   for letter in letters:
      char_dict = {"char": letter,"num":letters[letter]}
      chars_list.append(char_dict)
   return chars_list.sort(reverse=True, key=sort_on_num)

def sort_on_num(items):
   return items["num"]
      