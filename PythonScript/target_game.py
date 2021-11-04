from typing import List
import random


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['i', 'g', 'e'], ['p', 'i', 's'], ['w', 'm', 'g']]
    """
    ascii_lb = 97
    ascii_ub = 122
    list_of_lists = []
    for i in range(3):
        list_of_letters = []
        for j in range(3):
            rand_letter_code = random.randint(ascii_lb, ascii_ub)
            list_of_letters.append(chr(rand_letter_code))
        list_of_lists.append(list_of_letters)
    return list_of_lists


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words = []
    with open(f, "r") as file:
        lines = file.readlines()
        for i in range(3, len(lines)):
            words.append(lines[i])
    return words


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = []
    try:
        input_str = input('>>> ')
        while input_str != "":
            words.append(input_str.lower())
            input_str = input('>>> ')
    except EOFError:
        return words
    return words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_words = []
    occurred_letters = []

    letters_str = "".join(letters)
    letters_c = letter_count(letters_str)
    for user_word in user_words:
        if user_word+'\n' in words_from_dict and len(user_word) >= 4:
            word_letters_count = letter_count(user_word)

            success = True
            for (letter1, count1) in word_letters_count:
                if letter1 not in letters_str:
                    success = False
                    break

                for (letter2, count2) in letters_c:
                    if letter1 == letter2 and letter1 not in occurred_letters:
                        if count1 > count2:
                            success = False
                            break
                        occurred_letters.append(letter2)
            if success:
                pure_words.append(user_word)
    return pure_words


def results():
    grid = generate_grid()
    list_grid = []
    for list1 in grid:
        for letter in list1:
            list_grid.append(letter)
    print(list_grid)
    dict_words = get_words("en.txt", list_grid)
    user_words = get_user_words()
    pure_words = get_pure_user_words(user_words, list_grid, dict_words)
    print(pure_words)
    with open("result.txt", "w") as file:
        file.writelines("\n".join(pure_words))


def letter_count(word: str):
    list_of_tuples = []
    occured_letters = []
    for i in range(len(word)):
        letter = word[i]
        count = 1
        if letter in occured_letters:
            continue
        for j in range(i + 1, len(word)):
            if word[j] == letter:
                count += 1
        occured_letters.append(letter)
        list_of_tuples.append((letter, count))
    return list_of_tuples


if __name__ == "__main__":
    results()
