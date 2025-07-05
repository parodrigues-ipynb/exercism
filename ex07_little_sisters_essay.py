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
In this exercise you are helping your younger sister edit her paper
for school.

The teacher is looking for correct punctuation, grammar and excelent
word choice.

You have four tasks to clean up and modify strings.
"""

# 1. Capitalize the title of the paper
"""
Any good paper needs a properly formatted title.

Implement the function capitalize_title(<title>) which takes a title
<str> as a parameter and capitalizes the first letter of each word.

This function should return a <str> in title case.
"""


def capitalize_title(title):
    """
    Capitalizes the first letter of each word in the passed-in title.

    Args:
        title (str): The title of the paper.

    Returns:
        str: The title of the paper with the first letter of each word capitalized.

    Examples:
        >>> capitalize_title('my hobbies')
        'My Hobbies'
    """
    return title.title()

    # Improved version
    """
    If we pass the string "john's car" to capitalize_title(), it becomes
    "John'S Car".

    To avoid this, we could do the following:
    return ' '.join(word.capitalize() for word in title.split())

    title.split()   -> ["john's", "car"]
    word.capitalize -> ["John's", "Car"]
    ' '.join()      -> John's Car
    .                        ^ inserts the ' ' (space)
    """


# 2. Check if each sentence ends with a period
"""
You want to make sure that the punctuation in the paper is perfect.

Implement the function check_sentence_ending(<sentence>) that takes
<sentence> as a parameter. This function shoul return a bool.
"""


def check_sentence_ending(sentence):
    """
    Check if the passed-in sentence ends with a period (.).

    Args:
        sentence (str): The sentence to be checked.

    Returns:
        bool: True if the sentence ends with '.', False otherwise.

    Examples:
        >>> check_sentence_ending('This is the end.')
        True
    """
    return sentence.endswith('.')


# 3. Clean up spacing
"""
To make the paper look professional, unecessary spacing needs to be
removed.

Implement the function clean_up_spacing() that takes sentence as a
parameter.

The function should remove extra whitespace at both the beginning and
the end of the sentence, returning a new, updated sentence str.
"""


def clean_up_spacing(sentence):
    """
    Removes extra whitespace at both the beginning and the end of
    the passed-in sentence.

    Args:
        sentence (str): Sentence to be formated.

    Returns:
        str: A new string formatted without unnecessary whitespaces.

    Example:
        >>> clean_up_spacing('   The day is cold.      ')
        'The day is cold.'
    """
    return sentence.strip()   # .strip() removes whitespace by default


# 4. Replace words with a synonym
"""
To make the paper even better, you can replace some of the adjectives with
their synonyms.

Write the function replace_word_choice() that takes <sentence>, <old_word>
and <new_word> as parameters. This function should replace all instances
of <old_word> with <new_word> and return a new string with the updated sentence.
"""


def replace_word_choice(sentence, old_word, new_word):
    """
    Replaces all occurrences of a word with another word in a passed-in string.

    Args:
        sentence (str): The sentence where the word will be replaced.
        old_word (str): Word to be replaced.
        new_word (str): Word to take its place.

    Returns:
        str: A new string with the old word replaced by the new word.

    Example:
        >>> replace_word_choice('The cake is good', 'good', 'a lie')
        'The cake is a lie'
    """
    return sentence.replace(old_word, new_word)
