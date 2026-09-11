
import sys
from stats import get_book_word_count
from stats import character_count
from stats import char_dict_to_list

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    f= sys.argv[1]
    wordcount = get_book_word_count(f)
    characterdic = char_dict_to_list(character_count(f))

    def print_report(f, wordcount, characterdic):
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {f}...')
        print('----------- Word Count ----------')
        print(f'Found {wordcount} total words')
        print('--------- Character Count -------')
        for char in characterdic:
            letter = char[0]
            number = char[1]
            if letter.isalpha():
                print(f'{letter}: {number}')
            else:
                continue
        print('============= END ===============')

    def main():
        return print_report(f,wordcount,characterdic)



main()