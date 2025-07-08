# Personal notes
"""
This learning exercise helped you evolve your knowledge of List Methods.

List methods alter the list object that is being manipulated upon. If you
do not wish to mutate the original list, you will need to at least make
a shallow copy of it via slice or <list>.copy().

<list>.append() adds an item to the end or "right-hand side" of an existing list.
>>> numbers = [1, 2, 3]
>>> numbers.append(9)
>>> numbers
[1, 2, 3, 9]
>>> numbers = [1, 2, 3]
>>> other_numbers = [4, 5, 6]
>>> numbers.append(other_numbers)
>>> numbers
[1, 2, 3, [4, 5, 6]]

<list>.insert(<index>, <item>) can add an <item> at the specified <index>.
>>> numbers = [1, 2, 4]
>>> numbers.insert(2, 3)
>>> numbers
[1, 2, 3, 4]
#0  1  2  3   indexes

<list>.extend(<item>) combine existing list with the elements from another iterable.
The iterable is unpacked and elements are appended in order.
>>> numbers = [1, 2, 3]
>>> other_numbers = [4, 5, 6]
>>> numbers.extend(other_numbers)
>>> numbers
[1, 2, 3, 4, 5, 6]

<list>.remove(<item>) removes an item from a list. It throws a value error if the item
is not present in the list.
>>> numbers = [1, 2, 3]
>>> numbers.remove(2)
>>> numbers
[1, 3]

<list>.pop(<index>) removes an item an returns its value for use. Not specifying an
index will pop the last element.
>>> numbers = [1, 2, 3]
>>> numbers.pop(0)
1
>>> numbers
[2, 3]
>>> numbers.pop()
3

<list>.clear() clears the list.
>>> numbers = [1, 2, 3]
>>> numbers.clear()
>>> numbers
[]

<list>.reverse() reverse the order of elements in-place.
>>> numbers = [1, 2, 3]
>>> numbers.reverse()
>>> numbers
[3, 2, 1]

<list>.sort() sorts the elements in-place. Python has many arguments
to change the sorting effect desired.
>>> names = ['Marley', 'Bob', 'Zakk', Wylde']
>>> names.sort()
>>> names
['Bob', 'Marley', 'Wylde', 'Zakk']

The built-in function sorted() returns a copy of the list to sort, without
mutating the original list.
>>> names = ['Marley', 'Bob', 'Zakk', Wylde']
>>> sorted(names)
['Bob', 'Marley', 'Wylde', 'Zakk']
>>> names
['Marley', 'Bob', 'Zakk', Wylde']

<list>.count(<item>) counts the total number of times that <item> appears in
the <list>.
>>> items = [1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> items.count(1)
3

<list>.index(<item>) returns the index number of the first occurrence of an
item passed in. <start> and <end> indices can also be provided to narrow the search.
   <start> is inclusive
   <end>   is exclusive.
   e.g.   start <= index < end
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> numbers.index(2, 1, 2)
1
"""

# Instructions
"""
Chaitana owns a very popular theme park. She only has one ride in the very center of
beautifully landscaped grounds: The Biggest Roller Coaster in the World.

Although there is only this one attraction, people travel from all over the world and
stand in line for hours for the opportunity to ride Chaitana's hypercoaster.

There are two queues for this ride, each represented as a list:
* Normal Queue
* Express Queue - where people pay extra for priority access

You have been asked to write some code to better manage the guests at the park.
You need to implement the following functions as soon as possible before the guests
(and your boss, Chaitana!) get cranky.

Make sure you read carefully. Some tasks ask that you change or update the existing queue,
while others ask you to make a copy of it.
"""

# 1. Add me to the queue
"""
Define the add_me_to_the_queue() function that takes 4 parameters:
<express_queue>
<normal_queue>
<ticket_type> is an int with 1 == express_queue and 0 == normal_queue
<person_name> is a string of the person to be added to the respective queue
"""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """
    Adds the passed in <person_name> to the respective queue type of <ticket_type>.

    Args:
        express_queue (list): Current express queue.
        normal_queue (list): Current normal queue.
        ticket_type (int): 1 == express_queue, 0 == normal_queue.
        person_name (str): Person name to be added to the respective queue.

    Returns:
        list: Either <express_queue> or <normal_queue> with the person name added.

    Examples:
        add_me_to_the_queue(['Bob'], ['Melinda'], 1, 'Paulo')
        ['Bob', 'Paulo']
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue

    # Cool solution from yawpitch
    """
    queue = (normal_queue, express_queue)[ticket_type]
    queue.append(person_name)
    return queue

    
    Yawpitch uses a tuple and atributes the respective queue to the variable
    based on the value in ticket_type. Really cool!
    """

    # Solution from IsaacG's
    """
    if ticket type == 0:
        queue = normal_queue
    else:
        queue = express_queue
    return queue + [person_name]

    
    What intrigued me was the return line.

    >>> queue = ['Zelda', 'Link', 'Mario']
    I thought that
    >>> queue + ['Yoshi']
    should return
    ['Zelda', 'Link', 'Mario', ['Yoshi']]
    but, instead, it returns
    ['Zelda', 'Link', 'Mario', 'Yoshi']

    So I experimented the following
    >>> queue_1 = ['Zelda', 'Link', 'Mario']
    >>> queue_2 = ['Yoshi', 'Bowser']
    >>> queue_1 + queue_2
    ['Zelda', 'Link', 'Mario', 'Yoshi', 'Bowser']
    >>> queue_1.append(queue_2)
    ['Zelda', 'Link', 'Mario', ['Yoshi', 'Bowser']]

    And I see now:
    <list>.append(<list>) = [[]]
    <list> + <list> = []
    """

    # Solution from BethanyG
    """
    result = express_queue if ticket type == 1 else normal_queue
    result.append(person_name)
    return result


    I liked the first line. I didn't know you could atribute variables in Python
    like that.
    """


# 2. Where are my friends?
"""
One person arrived late at the park but wants to join the queue where
their friends are waiting. But they have no idea where their friends
are standing and there isn't any phone reception to call them.

Define the find_my_friend() function that takes 2 parameters: <queue>
and <friend_name> and returns the position in the queue of person's
name.

* <queue> is the list of people standing in the queue;
* <friend_name> is the name of the friend whose index (place in the
  que) you need to find.
"""


def find_my_friend(queue, friend_name):
    """
    Returns the 0-based index position of <friend_name> in the passed in
    list <queue>.

    Args:
        queue (list): List of the names of persons in the passed in queue.
        friend_name (str): Name to search in <queue>.

    Returns:
        The 0-based index position of <friend_name> in the passed in list
        <queue>, 'Not found' if <friend_name> is not an element of <queue>.

    Examples:
        >>> find_my_friend(['Bob', 'Melinda'], 'Melinda')
        1
        >>> find_my_friend(['Bob', 'Melinda'], 'Marley')
        'Not found'       
    """
    if friend_name in queue:
        return queue.index(friend_name)
    return 'Not found'


# 3. Can I please join them?
"""
Now that their friends have been found (in task #2 above), the late
arriver would like to join them at their place in the queue.

Define the add_me_with_my_friends() function that takes 3 parameters:
<queue>
<index>
<person_name>

Return <queue> updated with the late arrivals name.
"""


def add_me_with_my_friends(queue, index, person_name):
    """
    Returns the passed in <queue> updated with <person_name> inserted
    in the argument <index>.

    Args:
        queue (list): List of people standing in the queue.
        index (int): Position at which the new person should be added.
        person_name (str): Name of the person to add at the index position.

    Returns:
        list: <queue> updated with <person_name> inserted in the argument <index>.

    Example:
        >>> add_me_with_my_friends(['Bob', 'Marley', 'Lee'], 1, 'Skunk')
        ['Bob', 'Skunk', 'Marley', 'Lee']
    """
    queue.insert(index, person_name)
    return queue


# 4. Mean person in the queue
"""
You just hard from the queue that there is a really mean person shoving,
shouting and making trouble. You need to throw that miscreant out for
bad behavior!

Define the remove_the_mean_person() function that takes 2 parameters, <queue>
and <person_name>.

Return the queue updated without the mean person's name.
"""


def remove_the_mean_person(queue, person_name):
    """
    Removes the mean person (`person_name`) from the passed in `queue`.

    Args:
        queue (list): List of names of people in queue.
        person_name (str): Name of the mean person.

    Returns:
        The queue updated without the mean person.
    """
    if person_name in queue:
        mean_person = queue.index(person_name)
        queue.pop(mean_person)
    return queue

    # Cleaner solution
    """
    if person_name in queue:
        queue.remove(person_name)
    return queue
    """


# 5. Namefellows
"""
You may not have seen two unrelated people who look exactly the same,
but you have definitely seen unrelated people with the exact same name.
Namefellows!

Today, it looks like there are a lot of them in attendance. You want to know
how many times a particular name occurs in the queue.

Define the how_many_namefellows() function that takes 2 parameters:
<queue>
<person_name>

Return the number of occurrences of person_name as an integer.
"""


def how_many_namefellows(queue, person_name):
    """
    Counts the number of occurrences of person_name in the passed in queue.

    Args:
        queue (list): List containing the names of persons in the queue.
        person_name (str): Name of the person to be counted.

    Returns:
        int: Number of occurrences of the name in queue.

    Examples:
        >>> how_many_namefellows(['Bob', 'Marley', 'Bob'], 'Bob')
        2
        >>> how_many_namefellows(['Bob', 'Marley', 'Bob'], 'Ziggy')
        0
    """
    return queue.count(person_name)

    # Cool alternative way
    """
    return sum(1 for n in queue if person_name == n)


    You for sure doesn't need to do it this way, but it's cool.
    """

    # Another way using Boolean
    """
    sum ([person_name == person for person in queue])


    Who would've thought! You can sum booleans. What a cool idea.
    """


# 6. Remove the last person
"""
Sadly, it's overcrowed at the park today and you need to remove the last
person in the normal line (you will give them a ticket to come back in the
express queue on another day).

You will have to define the function remove_the_last_person() that takes 1
parameter 'queue', which is the list of people standing in the queue.

You should update the list and also return the name of the person who was removed,
so you can write them a voucher.
"""


def remove_the_last_person(queue):
    """
    Removes the last person from the passed in queue and returns its name.

    Args:
        queue (list): List of names of people in the queue.

    Returns:
        str: Name of the person removed from the queue.

    Examples:
        >>> queue = ['Bob', 'Ziggy', 'Marley']
        >>> remove_the_last_person(queue)
        'Marley'
        >>> queue
        ['Bob', 'Ziggy']
    """
    return queue.pop()


# 7. Sort the queue list
"""
For administrative purposes, you need to get all the names in a given queue
in alphabetical order.

Define the sorted_names() function that takes 1 argument, `queue`, (the `list`
of people standing in the queue) and turns a `sorted` copy of the `list`.
"""


def sorted_names(queue):
    """
    Returns a alphabetically sorted copy of the passed in queue.

    This function doesn't change the order of the original queue.

    Args:
        queue (list): List of names of the people in queue.

    Returns:
        list: Alphabetically sorted copy of the passed in queue.

    Example:
        >>> queue = ['Ziggy', 'Marley', 'Bob', 'Anna']
        >>> sorted_names(queue)
        ['Anna', 'Bob', 'Marley', 'Ziggy']
        >>> queue
        ['Ziggy', 'Marley', 'Bob', 'Anna']
    """
    return sorted(queue)
