# Project

The project will consist of two parts. The first part is to develop a
tree-based *lexicon* (dictionary) that can be used to check words,
detect spelling errors and make word suggestions. The second part is to
integrate these features into the Editor from Assignment 6.

## Tries

Read through the theory about tries: [file:tries.pdf](tries.pdf)

## Class `Trie` and basic operations.

Create a class `Trie` that implements the operations in the abstract
class `Lexicon`. It will use the trie nodes described above. The
important part of your node design is correctly storing the child nodes
to be able to access them by alphabet characters.

Implement `add` and `__contains__`.

### Operation `add`.

Adds a word to the lexicon. It has a single parameter `word`: the word
to add to the lexicon.

Implement the `add` operation using recursion.

### Operation `__contains__`.

Check if a word is in the lexicon. It has a single parameter `word`: the
word to check. True if the word is in the lexicon, False otherwise.

Implement the `__contains__` operation using recursion.

## Spell checking

Code a method `spell_check`, that checks the spelling for a text and
produces a list of spelling errors by location.

To check spelling, we will accept text that is `Iterable[str]`, where
the strings are assumed to be single characters.

The method returns a list of spelling errors. Each is a tuple (start,
end) that is the location of the spelling error in the text. The two
values in the tuples are indices that are inclusive and 0-indexed.

You can implement the `spell_check` non-recursively.

## Suggestions

Code a method `suggestions` that produces a list of suggested words
given a prefix.

It has two parameters:

- `prefix`: the word prefix to all suggestiongs will begin with.
- `limit`: the maximum number of words to suggest.

and returns a list of word suggesting from the lexicon with the prefix.

## Verification

A small python program `verifications.py` is included with the starter
to test your `Trie` class and operations.

## Editor Integration

Using the class `TextBuffer` from Assignment 6 add the features
described in this section.

### Spell check buffer

Add a method `spell_check`, to the class `TextBuffer`.

Using the `Trie` class's `spell_check` method, check the spelling of the
text currently in the text buffer, starting from the first character in
the buffer.

For each character in an incorrectly spelled word, set their foreground
color to red:

``` python
c.fg_color = TYPO # or Color(255, 0, 0) 
```

The updated `Editor` has a new key-bind, `a`, that calls this new method
in command mode.

<style>
.point{
    animation: blinker 1s linear infinite;
    background-color:rgb(128,128,128);
}
.typo{
    color:rgb(255,0,0);
}
@keyframes blinker {
  50% {
    opacity: 0;
  }
}
</style>

For example the text:

<code>Lorem ipsum dolor sit amet</code>

would highlight the following spelling errors:

<code><span class="typo">Lorem</span> ipsum <span class="typo">dolor</span> sit <span class="typo">amet</span></code>

### Suggestion

Add a method `suggest_at_point`, to the class `TextBuffer`.

Using the `Trie` class's `suggestion` method, suggest up to 5 words for
the prefix of the word ending at point. Use the `PUNCTUATION` defined in
`Lexicon` to delimit the word.

The updated `Editor` has a new key-bind, `s`, that calls this new method
in command mode and displays the results under the editor.

For example the text:

<code>Lorem ipsum dolor sit ame<span class="point">t</span></code>

could give the following suggestions:

    ['amelia', 'ameliorate', 'ameliorated', 'ameliorating', 'amelioration']
