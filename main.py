import os

def main():
    
    # get directory where script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # construct the path tot he book file
    book_path = os.path.join(script_dir, "books", "frankenstein.txt")

    # check if the file exists
    if os.path.exists(book_path):
        with open(book_path, 'r') as f:
            file_contents = f.read()
    else:
        print(f"Error: The file {book_path} does not exist.")
    
    # counting words
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")

    # lowercase
    convert_lowercase = file_contents.lower()

    # call char_count
    total_char = char_count(file_contents)
    print("Character count: ")
    print(f"{total_char}")

    # convert dictionary to list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in total_char.items()]
    char_list.sort(reverse=True,key=sort_on)
    for char_info in char_list:
        char = char_info['char']
        num = char_info['num']
        # only alphabetical characters
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")
       
def count_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def char_count(text):
    char_dict = {}
    lowercase_char = text.lower()
    for char in lowercase_char:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

# a function that takes a dictionary and returns the value of the "num" key
# this is how the '.sort()' mathod knows how to sort the list of dictionaries
def sort_on(char_dict):
    return char_dict["num"]

if __name__ == "__main__":
    main()