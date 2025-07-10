# Personal notes
"""
This learning exercise helped evolve your knowledge of Loops.

* `while` loops for indefinite (uncounted) iteration;
* `for` loops for definite (counted) iteration.

`break`, `continue` and `else` help customize loop behavior.

`range()` and `enumerate()` help with loop counting and indexing.

-----------------------------------------------------------------

A cool usage for while is the following:

>>> placeholders = ['spam', 'ham', 'eggs', 'green_spam']
>>> while placeholders:
...     print(placeholders.pop())
...
'spam'
'ham'
'eggs'
'green_spam'

-----------------------------------------------------------------

word_list = ['bird', 'chicken', 'barrel', 'bongo']

>>> for word in word_list:
...     if word.startswith('b'):
...         print(f'{word.title()} starts with a B.')
...     else:
...         print(f'{word.title()} doesn't start with a B.')
...
'Bird starts with a B.'
'Chicken doesn't start with a B.'
'Barrel starts with a B.'
'Bongo starts with a B.'

-----------------------------------------------------------------

`range()` requires an `int` before which to `stop` the sequence.
>>> for i in range(2):
...     print(i)
... 
0
1

You can optionally provide a `start` and a `step` parameters.

>>> for number in range(1, 4):
...     if number % 2 == 0:
...         print(f'{number} is even.')
...     else:
...         print(f'{number} is odd.')
...
'1 is odd.'
'2 is even.'
'3 is odd.'

-----------------------------------------------------------------

`enumerate()` is a built-in function that returns both (index, value).
"""


# Instructions
"""
You are a teaching assistant correcting student exams.

Keeping track of result manually is getting both tedious and
mistake-prone.

You decide to make things a little more interesting by putting
together some functions to count and calculate results for the
class.
"""


# 1. Rounding scores
"""
While you can give "partial credit" on exam questions, overall
exam scores have to be `integers`.

So, before you can do anything else with the class scores, you
need to go through the grades and turn any `float` scores into
`integers`.

Lucky for you, Python has built-in function `round()` you can use.

Create the function `round_scores(student_scores) that takes a
`list` of `student_scores`.

This function should CONSUME the input `list` and `return` a new
list with all the scores converted to `integers`.

The order of the scores in the resulting `list` is not important.
"""


def round_scores(student_scores):
    """
    Transforms the scores in the passed-in list `student_scores`
    into integers.

    Args:
        student_scores (list): List of the student scores.

    Returns:
        list: A copy of `student_scores` with all scores transformed
        into integers.

    Example:
        >>> round_scores([3.0, 5.2, 5.7])
        [3, 5, 6]
    """
    return [round(score) for score in student_scores]

    # Working explanation
    """
    for score in student_scores -> iterates through the list and gets
    .                              3.0, 5.2, 5.7

    round(score)                -> rounds and already converts to integers
    .                                3,   5,   6

    [<function here>]           -> list comprehension to return a list
    .                              [3, 5, 6]
    """


# 2. Non-passing students
"""
As you were grading the exam, you noticed some students weren't
perfoming as well as you had hoped. But you were distracted and
forgot to not exactly how many students.

Create the function `count_failed_students(student_scores)` that
takes a `list`of `student_scores`.

This function should count up the number of students who don't
have passing scores and return that count as an integer. A student
needs a score greater than 40 to achieve a passing grade on exam.
"""


def count_failed_students(student_scores):
    """
    Counts how many students in the passed-in list `student_scores`
    have a failing score (lesser than or equal to 40).

    Args:
        student_scores (list): List of all student scores.

     Returns:
        int: The number of scores less than or equal to 40 in the
        passed-in list `student_scores`.

    Example:
        >>> count_failed_students([40, 39, 41])
        2
    """
    return sum(score <= 40 for score in student_scores)

    # Working explanation
    """
    for score in student_scores -> gets the elements in the list
    .                              40, 39, 41

    score <= 40                 -> checks how many scores are smaller
    .                              or equal to 40
    .                              True, True, False

    sum()                       -> sums the boolean values. True = 1, False = 0
    .                                 1,    1,     0
    .                              2
    """


# 3. The "best"
"""
The teacher you are assisting wants to find the group of students
who have perfomed "the best" on this exam.

What qualifies as "the best" fluctuates, so you need to find the
student scores that are greater than or equal to the current threshold.

Create the function above_threshold(student_scores, threshold) taking
`student_scores`, a list of grades, and `threshold`, the top score threshold.

This function should return a `list` of all scores that are >= to `threshold`.
"""


def above_threshold(student_scores, threshold):
    """
    Returns a list of the best scores in the passed-in list of student scores.
    "Best" qualifies as greater than or equal to the passed-in threshold.

    Args:
        student_scores (list): List of the all student scores.
        threshold (float): The top score threshold.

    Returns:
        list: Scores greater than or equal to the given threshold.

    Example:
        >>> above_threshold([2, 3, 1], 3)
        [3]
    """
    return [score for score in student_scores if score >= threshold]

    # Working explanation
    """
    [<function here>] is called list comprehension.

    [score for score in student_scores if score >= threshold]

    This line of code is equal to:

    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    """


# 4. Calculating letter grades
"""
The teacher you are assisting likes to assign letter grades as well as
numeric scores. Since students rarely score 100 on an exam, the "letter
grade" lower thresholds are calculated based on the highest score achieved,
and increment evenly between the high score and the failing threshold of <= 40.

Create the function `letter_grades(highest)` that takes the "highest" score on
the exam as an argument and returns a `list` of lower score thresholds for each
"American style" grade interval: D, C, B, A.
"""


def letter_grades(highest):
    """
    Returns a list of grades thresholds based upon the highest score provided.

    Args:
        highest (int): The highest score obtained in the exam.

    Returns:
        list: List of mininum score needed for each grade, in order [D, C, B, A].

    Example:
        >>> letter_grades(88)
        [41, 53, 65, 77]
    """
    num_of_grades = 4
    fail_threshold = 40

    delta = (highest - fail_threshold) // num_of_grades

    return [(fail_threshold + 1) + delta * grade for grade in range(num_of_grades)]

    # Working explanation
    """
    The function works as following:

    ----------------------------------------------------
    num_of_grades = 4
    fail_threshold = 40

    delta = (highest - fail_threshold) // num_of_grades

    score_thresholds = []
    for grade in range(num_of_grades):
        score_thresholds.append(41 + delta * grade)
    return score_thresholds
    ----------------------------------------------------

    But we used list comprehension to make it more concise.
    """

    # Elegant solution by jeefparker
    """
    gap = round((highest - 41) / 4) 
    return list(range(41, highest, gap))

    
    What an elegant solution!
    round() is better than // because
    4.9 / 3         ->  1.6333333335
    round(4.9 / 3)  ->  2
    4.9 // 3        ->  1.0

    And then they adress the problem with the step parameter!
    What a genius solution!
    """


# 5. Matching names to scores
"""
You have a list of exam scores in descending order, and another list of student names
also sorted in descending order by their exam scores.

You would like to match each student name with their exam score and print out an overall
class ranking.

Create the function student_ranking(student_scores, student_names). Match each student
name with their score.
"""


def student_ranking(student_scores, student_names):
    """
    Matches the provided student scores with the respective student names.

    This function assumes both provided lists are in descending order.

    Args:
        student_scores (list): Student scores in descending order.
        student_names (list): Student names in descending order.

    Returns:
        list: Student scores matched with their respective student name.

    Example:
        >>> student_ranking([100, 97, 95], ['zelda', 'bob', 'ziggy'])
        ['1. zelda: 100', '2. bob: 97', '3. ziggy: 95']
    """
    return [f'{index + 1}. {name}: {score}' for index, (name, score) in enumerate(zip(student_names, student_scores))]

    # Working explanation
    """
    a = [100, 97, 95]
    b = ['bob', 'ziggy', 'zelda']

    zip(a, b)                 ->  <zip object at MEMORY_SLOT>
    list(zip(a,b))            ->  [(100, 'bob'), (97, 'ziggy'), (95, 'zelda')]

    enumerate(zip(a,b))       ->  <enumerate object at MEMORY_SLOT>

    for index, (name, score)  ->  [(100, 'bob'), (97, 'ziggy'), (95, 'zelda')]
    .                                   0             1               2
    """


# 6. A "perfect" score
"""
Although a "perfect" score of 100 is rare on an exam, it is interesting to know if
at least one student has achieved it.

Create the function perfect_score(student_info).

`Student_info` is a `list` of lists containing the name and score of each student.
[["Charles", 90], ["Tony" 80]]

The function should return the first pair of the student who scored 100 on the exam.

If no 100 scores are found in `student_info`, an empty list [] should be returned.
"""


def perfect_score(student_info):
    """
    Returns the first pair of score and student in the provided list which has a
    perfect score (100).

    Args:
        student_info (list): Names and scores of students organized in lists.

    Returns:
        list: The first list of [name, score] with a score of 100 found in the
        provided student_info.

    Example:
        >>> perfect_score([['bob', 100], ['zelda', 2], ['ziggy', 100]])
        ['bob', 100]
    """
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
