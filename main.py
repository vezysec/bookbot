def get_book_text(file_path):
    with open(file_path,"r") as f:
        return f.read()
    
def count_words(text):
    number = len(text.split())
    return number

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

main()