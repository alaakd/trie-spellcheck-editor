from typing import Optional, Iterator, Iterable


DEFAULT_WORDS_FILE = "words-linux-cleaned.txt"
PUNCTUATION = "!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\" \n\0"


class Lexicon:
    def add(self, word: str):
        """ Add a word to the lexicon.

        :param word: the word to add to the lexicon.
        """


    def __contains__(self, word: str) -> bool:
        """ Check if a word is in the lexicon.
        
        :param word: the word to check.
        :returns: True if the word is in the lexicon, False otherwise.
        """

    def spell_check(self, text: Iterable[str]) -> list[tuple[int, int]]:
        """ Check the spelling for a text and produce a list of spelling errors by location.

        :param text: the text to check for spelling errors, as an iterable of single characters.
        :returns: a list of spelling errors. Each is a tuple (start, end) that is the location of the spelling error, both inclusive and 0-indexed.        
        """
        

    def suggestions(self, prefix: str, limit: int) -> list[str]:
        """Produce a list of suggested words given a prefix.

        :param prefix: the word prefix to all suggestions will begin with.
        :param limit: the maximum number of words to suggest.
        :returns: a list of word suggesting from the lexicon with the prefix.
        """
