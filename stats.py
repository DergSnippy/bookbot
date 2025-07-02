def word_count(text):
    words = text.split()
    print(f"{len(words)} words found in the document")

def char_count(text):
    low_text = text.lower()
    char_dict = {}
    for char in low_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    for char in char_dict:
        print(f"''{char}': {char_dict[char]}'")