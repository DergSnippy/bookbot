def word_count(text):
    words = text.split()
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")

def char_count(text):
    print("----------- Character Count ----------")
    low_text = text.lower()
    char_dict = {}
    for char in low_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    for char in char_dict:
        print(f"{char}: {char_dict[char]}")

def sorted_char_count(text):
    print("----------- Character Count ----------")
    low_text = text.lower()
    char_dict = {}
    for char in low_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    sorted_chars = sorted(char_dict.items(), key=lambda item: item[0])
    for char, count in sorted_chars:
        print(f"{char}: {count}")