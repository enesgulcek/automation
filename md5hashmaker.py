import hashlib
import itertools

def hash_maker(word_list, num_letters=3, allow_repeats=False):
    """
Diese Funktion nimmt eine Liste von Wörtern und generiert mit der MD5-Hash-Funktion einen Hash für jede mögliche Buchstabenkombination. Wenn num_letters angegeben wird, wird nur diese Anzahl von Buchstaben aus jedem Wort verwendet. Wenn allow_repeats True ist, können Buchstaben in den Kombinationen wiederholt werden.
    """
    for word in word_list:
        if num_letters is None:
            letter_range = range(1, len(word)+1)
        else:
            letter_range = [num_letters]
        for r in letter_range:
            if allow_repeats:
                combinations = itertools.product(word, repeat=r)
            else:
                combinations = itertools.combinations(word, r)
            for combination in combinations:
                string = ''.join(combination)
                hashed_string = hashlib.md5(string.encode()).hexdigest()
                print(f"{string}: {hashed_string}")

# Example usage:
word_list = ['abcde12345']
hash_maker(word_list)  # Hash alle Buchstabenkombinationen jedes Wortes
#hash_maker(word_list, num_letters=3)  # Hash nur 3-Buchstaben-Kombinationen jedes Wortes
#hash_maker(word_list, allow_repeats=True)  # Hash alle Buchstabenkombinationen jedes Wortes mit Wiederholungen
#hash_maker(word_list, num_letters=3, allow_repeats=True)  # Hash nur 3-Buchstaben-Kombinationen jedes Wortes mit Wiederholungen
