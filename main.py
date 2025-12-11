from stats import count_words, count_each_char, sort_letters_by_count
import sys

def get_book_text(file_path):
    with open(file_path,"r") as f:
        return f.read()
    
def main():
    if len(sys.argv) > 1:
       book_path = sys.argv[1]
    else:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
       
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = sort_letters_by_count(count_each_char(book_text))
    for char_count in char_counts:
      if char_count["char"].isalpha():
        print(f"{char_count["char"]}: {char_count["num"]}")
    print("============= END ===============")

main()