VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def vowel_count(string):
    """ returns the frequency of vowels in the string """ 

    count = {}

    for letter in string:
        if letter in VOWELS:
            count[letter] = count.get(letter, 0) + 1

        return count
