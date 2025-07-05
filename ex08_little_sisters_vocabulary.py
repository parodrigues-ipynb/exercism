# Personal notes
"""
This learning exercise helped you evolve your knowledge of strings.

Concatenating strings using the + operator is available, but should
be used sparingly as it is not very perfomant or easily maintained.

If a list, tuple, set or another collection of individual strings
needs to be combined into a single string, <str>.join(<iterable>)
is a better option:
>>> chickens = ['hen', 'egg', 'chicken']
>>> ' '.join(chickens)
'hen egg chicken'

Substrings can be selected via slice notation:
<str>[<start> : stop : <step>]
>>> abba = 'ABABABA'
>>> abba[::2]
'AAAA'
>>> abba[:-3]
'ABAB'
>>> abba[1:-3]
'BAB'

<str>.split(<separator>) returns a list of substrings. If no arguments
are passed, the default ' ' (whitespace) separator will be applied.
>>> cat_ipsum = "Destroy house in 5 seconds mock the hooman."
>>> cat_ipsum.split()
['Destroy', 'house', 'in', '5', 'seconds', 'mock', 'the', 'hooman.']
>>> cat_ipsum.split()[-1]
'hooman.'
>>> cat_words = "feline, four-footed, ferocious, furry"
>>> cat_words.split(', ')
['feline', 'four-footed', 'ferocious', 'furry']
>>> colors = '''red,
orange,
green,
purple,
yellow'''
>>> colors.split(',\n')
['red', 'orange', 'green', 'purple', 'yellow']

>>> exercise = 'လေ့ကျင့်'

Strings are iterable objects and can be iterated through in a loop
via for item in <str>.
>>> for code_point in exercise:
...    print(code_point)
လ
ေ
့
က
ျ
င
်
့
>>> for index, code_point in enumerate(exercise):
...    print(index, ": ", code_point)
...
0 :  လ
1 :  ေ
2 :  ့
3 :  က
4 :  ျ
5 :  င
6 :  ်
7 :  ့

"""
# Instructions
"""
You are helping your younger sister with her English vocabulary
homework, which she is finding very tedious.

Her class is learning to create new words by adding prefixes and
suffixes.

Given a set of words, the teacher is looking for correctly
transformed words with correct spelling by adding the prefix to
the beggining and the suffix to the ending.

The assignment has four activities, each with a set of text or
words to work with.
"""

# 1. Add a prefix to a word
"""
One of the most common prefixes in English is 'un', meaning 'not'.
In this activity, your sister needs to make negative, or 'not' words
by adding 'un' to them.

Implement the add_prefix_un(<word>) function that takes word as a
parameter and returns a new un prefixed word.
"""


def add_prefix_un(word):
    """
    Adds the prefix 'un' to the beginning of the passed-in word.

    Args:
       word (str): Word to which the 'un' prefix will be added.

    Returns:
       str: 'un' + 'word'

    Examples:
       >>> add_prefix_un(funny):
       'unfunny'
       >>> add_prefix_un(manageable):
       'unmanageable'
    """
    return "un" + word


# 2. Add prefixes to word groups
"""
There are four more common prefixes that your sister's class is
studying:
* 'en',    meaning to 'put into' or 'cover with')
* 'pre',   meaning 'before' or 'forward')
* 'auto',  meaning 'self' or 'same')
* 'inter', meaning 'between' or 'among')

In this exercise, the class is creating groups of vocabulary words
using these prefixes, so they can be studdied together.

Each prefix comes in a list with common words it's used with. The
students need to apply the prefix and produce a string that shows
the prefix applied to all of the words.

Implement the make_word_groups(<vocab_words>) function that takes a
vocab_words as a parameter in the following form:
[<prefix>, <word_1>, <word_2>, ..., <word_n>]
and returns a string with the prefix applied to each word <w> that
looks like:
<prefix> :: <prefix><word_1> :: <prefix><word_2> :: ... :: <prefix><word_n>
"""


def make_word_groups(vocab_words):
    """
    Adds a prefix to a list of words.

    Args:
       vocab_words(list): List of prefix and words to which the prefix will be added.
       ['<prefix>', '<word_1>', ..., '<word_n>']

    Returns:
       str: Words with the prefix applied and grouped in the following pattern:
       '<prefix> :: <prefix><word_1> :: ... :: <prefix><word_n>'

    Examples:
       >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
       'en :: enclose :: enjoy :: enlighten'
       >>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
       'pre :: preserve :: predispose :: preposition'
    """
    prefix = vocab_words[0]
    # this is called 'list comprehension'
    words = [prefix + word for word in vocab_words[1:]]
    # vocab_words[1:] -> [<word_1>, <word_2>, ..., <word_n>]
    # for word in     -> gets <word_1>, then <word_2>... and stops after <word_n>
    # prefix + word   -> applies an uniformized action to each <word_x>
    # [ ]             -> atributes a list containing all the elements to 'words'
    return ' :: '.join([prefix] + words)
    # .join() requires lists. [prefix] is used to transform prefix (str) to a list
    #                         of 1 element

    # Really elegant solution by bobahop
    """
    return (' :: ' + vocab_words[0]).join(vocab_words)

    This solution astonished me for its elegance.
    .join(vocab_words)        -> <prefix>, <word_1>, <word_2>...
    (' :: ' + vocab_words[0]) -> adds ' :: <prefix>' between all elements
    Which results in
    <prefix> :: <prefix><word_1> :: ...

    Really cool! But it's worth stating that the words in vocab_words stay the same,
    without the prefix added to elements in the list.
    """


# 3. Remove a suffix from a word
"""
'ness' is a common suffix that means 'state of being'. In this activity, your sister
needs to find the original root word by removing the 'ness' suffix.

But of course there are pesky spelling rules:
if the root word originally ended in a consonant followed by an 'y', then the 'y'
needs to change to 'i'.

Removing 'ness' needs to restore the 'y' in those root words.
e.g. 'happiness' -> 'happy'

Implement the remove_suffix_ness(<word>) function that takes in a word and returns the
root word without the 'ness' suffix.
"""


def remove_suffix_ness(word):
    """
    Returns the passed-in word without the suffix 'ness'.

    Args:
       word (str): Word with the suffix 'ness' to be removed.

    Returns:
       str: Word without the 'ness' suffix.

    Examples:
       >>> remove_suffix_ness('happiness'):
       'happy'
       >>> remove_suffix_ness('delightfulness'):
       'delightful'
    """
    root = word[:-4]   # removes 'ness'
    if root.endswith('i'):
        root = root[:-1] + 'y'
    return root


# 4. Extract and transform a word
"""
Suffixes are often used to change the part of speech a word is
assigned to. A common practice in English is "verbing", or
"verbifying" - where an adjective becomes a verb by adding an
'en' suffix.

In this task, your sister is going to practice "verbing" words
by extracting an adjective from a sentence and turning it into
a verb.

Fortunatelly, all the words that need to be transformed here are
"regular" - meaning they don't need spelling changes to add the
suffix.

Implement the adjective_to_verb(<sentence>, <index>) function that
takes two parameters.

A <sentence> using the vocabulary word and the <index> of the word,
once that sentence is split apart. The function should return the
extracted adjective as a verb.
"""


def adjective_to_verb(sentence, index):
    """
    Transforms a given word in a passed-in sentence into a verb by
    adding 'en' to its end.

    Args:
       sentence (str): Sentence that contains the word to be "verbified".
       index (int): 0-based index of the word in the passed-in sentence.

    Returns:
       str: The word at the given index transformed into a verb by adding 'en'.

    Examples:

    >>> adjective_to_verb('I need to make that bright.', -1 )
    'brighten'
    >>> adjective_to_verb('It got dark as the sun set.', 2)
    'darken'
    """
    words = sentence.split()   # splits the str sentence into a list of words
    word = words[index].strip('.,;!?')
    # words[index] gets the word to be "verbified"
    # .strip('.,;!?') removes the most common punctuation symbols
    # a better solution might would've been adding the library string
    # and then using .strip(string.punctuation)
    return word + 'en'
