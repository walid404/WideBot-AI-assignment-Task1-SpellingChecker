class SpellingChecker:

    def __init__(self, dictionary: list):
        self._sorted_word_list = sorted(list(dictionary))


    def nearest4Words(self, word: str) -> list:
        '''
        Return the nearest 4 words from the given word by lexicographic order.
        :param word: word that we want to find nearest for word to it.
        :return nearest_4: list of nearest 4 words and empty list if word not founded
        in dictionary.
        Space Complexity = n
        Time Complexity = n
        '''
        nearest_4 = []
        if word in self._sorted_word_list:
            word_index = self._sorted_word_list.index(word)

            if word_index + 3 <= len(self._sorted_word_list) and word_index - 2 >= 0:
                nearest_4 = self._sorted_word_list[word_index - 2 : word_index]\
                            + self._sorted_word_list[word_index + 1 : word_index + 3]

            elif word_index == 0:
                nearest_4 = self._sorted_word_list[1:5]

            elif word_index == len(self._sorted_word_list) - 1:
                nearest_4 = self._sorted_word_list[-5:-1]

            elif word_index + 3 > len(self._sorted_word_list):
                nearest_4 = self._sorted_word_list[word_index - 3: word_index]\
                            + self._sorted_word_list[word_index + 1]
            elif word_index - 2 < 0:
                nearest_4 = self._sorted_word_list[word_index - 1]\
                            + self._sorted_word_list[word_index + 1 : word_index + 4]

        return nearest_4


    def addToWord(self, word: str):
        '''
        Add the given word in dictionary and sort it and save the dictionary.
        :param word: the word we want add it to dictionary
        :return: Nothing
        Space Complexity = n
        Time Complexity = n
        '''
        if word not in self._sorted_word_list:
            self._sorted_word_list.append(word)
            self._sorted_word_list = sorted(self._sorted_word_list)
            with open('dictionary.txt', 'w', encoding='latin-1') as file:
                for word in self._sorted_word_list:
                    file.write(word + '\n')



if __name__ == '__main__':
    dictionary = set()
    with open('dictionary.txt', 'r', encoding='latin-1') as file:
        for line in file:
            word = line[:-1]
            dictionary.add(word)

    dictionary = list(dictionary)
    checker = SpellingChecker(dictionary)
    checker.addToWord('waleed')
    print(checker.nearest4Words('waleed'))