import hashlib
import itertools

def hash_maker(word_list, num_letters=3, allow_repeats=True, hash_algorithm='sha1'):
    """
  Diese Funktion nimmt eine Liste von Wörtern und generiert einen Hash für jede mögliche Buchstabenkombination unter Verwendung des angegebenen Hash-Algorithmus. Wenn num_letters angegeben wird, wird nur diese Anzahl von Buchstaben aus jedem Wort verwendet. Wenn allow_repeats True ist, können Buchstaben in den Kombinationen wiederholt werden.
    """
    if hash_algorithm == 'md5':
        hasher = hashlib.md5
    elif hash_algorithm == 'sha1':
        hasher = hashlib.sha1
    elif hash_algorithm == 'sha256':
        hasher = hashlib.sha256
    else:
        raise ValueError("Invalid hash algorithm. Supported values are 'md5', 'sha1', and 'sha256'.")

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
                hashed_string = hasher(string.encode()).hexdigest()
                print(f"{string}: {hashed_string}")

# Beispielverwendung:
word_list = ['abcde12345']
hash_maker(word_list) # Hash alle Buchstabenkombinationen jedes Wortes mit MD5
hash_maker(word_list, num_letters=3) # Hash nur 3-Buchstaben-Kombinationen jedes Wortes mit MD5
hash_maker(word_list, allow_repeats=True) # Hash alle Buchstabenkombinationen jedes Wortes mit Wiederholungen unter Verwendung von MD5
hash_maker(word_list, num_letters=3, allow_repeats=True) # Hash nur 3-Buchstaben-Kombinationen jedes Wortes mit Wiederholungen unter Verwendung von MD5
hash_maker(word_list, hash_algorithm='sha1') # Hash alle Buchstabenkombinationen jedes Wortes mit SHA1
hash_maker(word_list, num_letters=3, hash_algorithm='sha256') # Hash nur 3-Buchstaben-Kombinationen jedes Wortes mit SHA256
