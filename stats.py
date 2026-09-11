def get_book_word_count(f):
        with open(f) as text:
            texts = text.read()
            word = texts.split()
            word_num =len(word)
            return word_num

char_count= {}
def character_count(f):
    with open(f) as text:
        texts=text.read()
    
    for c in texts:
        lowered = c.lower()
        if lowered in char_count:
            char_count[lowered] +=1
        else:
            char_count[lowered] = 1
    return char_count


        
def sort_on(charss_counter:tuple[str, int])-> int:
    return charss_counter[1]

def char_dict_to_list(char_count:dict[str, int]) -> list[tuple[str, int]]:
    lister = []
    for chars in char_count:
        number = char_count[chars]
        lister.append((chars,number))
    sorted_lister = sorted(lister, reverse=True, key=sort_on)
    return sorted_lister