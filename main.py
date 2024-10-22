import os

def main():
    # Change to the directory where your script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")
       
def count_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

if __name__ == "__main__":
    main()