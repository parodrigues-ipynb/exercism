# Personal notes
"""
This learning exercise helped evolve your knowledge of String Methods.

Strings are immutable sequences of Unicode code points. So any function
or method that operates on a str will return a new instance of that str
object instead of modifying the original str.

You can declare strings with:
* Single quotes: ''
* Double quotes: ""
* Triple quotes: '''''' or """"""

Triple quoted strings can span multiple lines - all associated whitespace
will be included in the string literal.
>>> str = '''teste
... muito
... loco'''
>>> print(str)
teste
muito
loco
>>> str = '''
... teste
... muito
... loco
... '''
>>> print(str)

teste
muito
loco

>>> print('''
... there is a space here -> 
... ''')
there is a space here ->    # the space really shows up

Individual "characters", or code points (strings of length 1) can be
referenced by 0-based index number from the left, or -1-based index
number from the right.
>>> str = "joaozinho"
>>> str[0]
'j'
>>> str[-1]
'o'
>>> 

Strings can be iterated through using 'for item in <str>', or
'for index, item in enumerate(<str>)' syntax.
>>> str = "link"
>>> for letter in str:
...     print(letter)
l
i
n
k
>>> for index, letter in enumerate(str):
...     print("index:", index, "letter:", letter)
index: 0 letter: l
index: 1 letter: i
index: 2 letter: n
index: 3 letter: k

You can concatenate strings using the + operator or via
<string>.join(<iterable>)
>>> str1 = "ragnarok"
>>> str2 = "all night long"
>>> str = str1 + str2
>>> print(str)
ragnarokall night long
>>> str1 = "link"
>>> str2 = "zelda"
>>> str = str1.join(str2)
>>> str
'zlinkelinkllinkdlinka'
>>> str1 = "link"
>>> str = " ".join(str1)
>>> str
'l i n k'

<str>.title() capitalizes the first "character" of each "word" found.
>>> man_in_hat_th = 'ผู้ชายใส่หมวก'
>>> man_in_hat_th.title()
'ผู้ชายใส่หมวก'
>>> man_in_hat_ru = 'мужчина шляпе'
>>> man_in_hat_ru.title()
'Мужчина Шляпе'
>>> man_in_hat_ko = '모자를 쓴 남자'
>>> man_in_hat_ko.title()
'모자를 쓴 남자'
>>> man_in_hat_en = 'the man in the hat.'
>>> man_in_hat_en.title()
'The Man In The Hat.'

<str>.endswith(<suffix>) returns True if the string ends with <suffix>,
False otherwise.
>>> 'My heart breaks. 💔'.endswith('💔')
True
>>> 'cheerfulness'.endswith('ness')
True

<str>.strip(<chars>) returns a copy of the str with leading and trailing
<chars> removed. If nothing is specified for <chars>, all combinations of
whitespace code points will be removed.
>>> 'https://unicode.org/emoji/'.strip('/stph:')
'unicode.org/emoji'
>>> '   🐪🐪🐪🌟🐪🐪🐪   '.strip()
'🐪🐪🐪🌟🐪🐪🐪'
>>> justification = 'оправдание'
>>> justification.strip('еина')
'оправд'
# Prefix and suffix in one step.
>>> 'unaddressed'.strip('dnue')
'address'
>>> '  unaddressed  '.strip('dnue ')
'address'

<str>.replace(<substring>, <replacement substring>) returns a copy of
the string with all occurrences of <substring> replaced with the
<replacement substring>.
>>> quote = '''
"Just the place for a Snark!" the Bellman cried,
   As he landed his crew with care;
Supporting each man on the top of the tide
   By a finger entwined in his hair.

"Just the place for a Snark! I have said it twice:
   That alone should encourage the crew.
Just the place for a Snark! I have said it thrice:
   What I tell you three times is true."
'''

>>> quote.replace('Snark', '🐲')
...
'\n"Just the place for a 🐲!" the Bellman cried,\n   As he landed his crew with care;\nSupporting each man on the top of the tide\n   By a finger entwined in his hair.\n\n"Just the place for a 🐲! I have said it twice:\n   That alone should encourage the crew.\nJust the place for a 🐲! I have said it thrice:\n   What I tell you three times is true."\n'
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
