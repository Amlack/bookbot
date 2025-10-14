def get_num_words(text):
    total_words = text.split()
    return len(total_words)

def get_character_count(text):
    #characters{char: k, num, v}
    characters = {}
    lowercase = text.lower()

    for char in lowercase:
        characters[char] = characters.get(char, 0) + 1
    return characters

def sort_on(item):
    return item["num"]

def get_ordered_characters(characters):
    sorted_characters = []

    for k, v in characters.items():
        sorted_characters.append({"char": k, "num": v})
    sorted_characters.sort(key = sort_on, reverse = True) #/.sort/ - default in ascending order, thats why reverse = True
    return sorted_characters    