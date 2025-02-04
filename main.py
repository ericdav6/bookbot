def main ():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    

    words = count_words(file_contents)
    print(f"--- Begin report of {file_path} ---")
    print(f"{words} Words found in the document")

    char_count = count_chars(file_contents)
    for cur_char in char_count:
        if cur_char.isalpha():
            print(f"The '{cur_char}' was found {char_count[cur_char]} times.")
    
    print("--- End Report ---")

        
    
def count_words(file_content):
    return len(file_content.split())

def count_chars(file_content):
    char_dict = {}
    file_lowercase = file_content.lower()
    for word in file_lowercase:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


main()

