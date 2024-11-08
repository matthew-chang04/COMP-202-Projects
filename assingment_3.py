# Constants
STRING_SIZE_LIMIT = 1000
MIN_STRING_SIZE = 1

def deep_copy(list):
    '''
    Returns a deep copy of a 2D list
    (list) -> list

    Examples:
    deep_copy([['a','b','c'], ['d','e','f'], ['g', 'h', 'i']])
    >>> [['a','b','c'], ['d','e','f'], ['g', 'h', 'i']]

    deep_copy([[1,2,3], [4,5,6], [7,8,9]])
    >>> [[1,2,3], [4,5,6], [7,8,9]]

    deep_copy([[6,7,8],[4,5,6], [7,8,9],[8,9,'p']])
    >>> [[6,7,8],[4,5,6], [7,8,9],[8,9,'p']]
    '''
#   Creating an empty list to store the copy in.    
    new_list = []

#   Iterate through the list to access each sublist.
    for sublist in list:
        new_sublist = []

#   Iterating through each element of the sublist and appending it to the copy.
        for char in sublist:
            new_sublist.append(char)
        new_list.append(new_sublist)
    return new_list


def check_square(string):
    '''
    Verifies if the length of the input is a perfect square and if true, returns the root.

    (str) -> int

    Examples:

    check_square("apple")
    >>> 0

    check_square("name")
    >>> 2

    check_square("_ _ ")
    >>> 2
    '''
#    Note: Project constraints are that the square root function is not allowed, nor any non-integer exponents
    for index in range(len(string)):
        if index ** 2 == len(string):
            return index
    return 0
    

def is_not_valid(string):
    '''
    Returns true if a string has special characters.

    (str) -> bool

    Examples:

    is_not_valid("dog")
    >>> False

    is_not_valid("help__!")
    >>> True

    is_not_valid(" HeLoO   ")
    >>> False
    '''

#   Verify ASCII code of each character in the string. (isdecimal() and isalpha() methods are prohibited)
    for character in string:    
        if not(character >= "A" and character <= "Z" or character >= "a" and character <= "z" or character == " "):
            return True

    return False


def is_not_square(string):
    '''
    Identifies if the length of the input string is a perfect square.

    (str) -> bool

    Examples:

    is_not_square("home")
    >>> False

    is_not_square("KjSdJdIdf__T!!!!)
    >>> False

    is_not_square("TTT")
    >>> True
    '''
#   Calling check square function and converting it to a boolean
    return not(check_square(string))
            

def string2list(string):
    '''
    Returns a 2D list based on the input string with sublist lengths equal to the length of the list

    (str) -> list

    Examples:

    string2list("every one")
    >>> [['e','v','e'],['r','y',' '],['o','n','e']]

    string2list("Yes!")
    >>> []

    string2list("Not Square")
    >>> []
    '''
#   Prepare an empty list and check if the input string is of proper format.
    temp_list = []
    if is_not_valid(string) or is_not_square(string) or MIN_STRING_SIZE > len(string) or len(string) > STRING_SIZE_LIMIT:
        return temp_list

#   Parsing the string into a 1D list.    
    for index in string:
        temp_list.append(index)

#   Establishing the size of each sublist.
    sublist_len = check_square(string)
    list = []

#   Appending each sublist from the 1D list to the new 2D list.
    for index in range(sublist_len):
        list.append(temp_list[index * sublist_len: (index * sublist_len) + sublist_len])

    return list

def add_space(input_text):
    '''
    Returns the input text with spaces before every isolated uppercase letter.

    (str) -> str

    Examples:

    add_space("stRing")
    >>> st Ring

    add_space("HelloHowAReYou")
    >>> Hello HowARe You

    add_space("HellO")
    >>> HellO
    '''
#   Initialize a counter to track where each edit is made, a copy of the string to modify, and an empty string to add modifications to.   
    last_edit = 0
    string_copy = input_text
    output_text = ""

#   Iterate through each index in the string (skipping the first and last entries).
    for index in range(1,len(input_text) - 1):

#       Verify the current character is Uppercase, and both surrounding characters are lowercase.
        if input_text[index] <= "Z" and input_text[index - 1] >= 'a' and input_text[index + 1] >= 'a' and input_text[index + 1] != " " and input_text[index - 1] != " ":
            output_text += string_copy[last_edit:index] + " "
            last_edit = index

#   Concatenate the final string segment to the output string    
    output_text += string_copy[last_edit:]
    
    return output_text


def list2string(list):
    '''
    Converts an inputted 2D list to a string.
    
    (list) -> str
    
    Examples:
    list2string([['h','e','l'], ['o','W','o'],['r','l','d']])
    >>> "helo World"

    list2string([['h','E','l'], ['o','w','o'],['R','l','d']])
    >>> "h Elowo Rld"

    list2string([['h','o','c'], ['H','e','R'],['R','l','d']])
    >>> "hoc HeRRld"
    '''

#   Create an empty string to concatenate characters to
    string_result = ""

#   Iterate through the sublists in list to retreive each character.
    for sublist in list:
        for char in sublist:
            string_result += char

#   Apply the add_space() function to format the string.    
    return add_space(string_result)


def horizontal_flip(list):
    '''
    Edits the inputted 2D list so the order of characters within each sublist is reversed.
    
    (list) -> None
    
    Examples:
    
    horizontal_flip([['e','v','e'],['r','y',' '],['o','n','e']])
    >>> [['e', 'v', 'e'], [' ', 'y', 'r'], ['e', 'n', 'o']] 
    
    horizontal_flip([['a','b','c'],['d','e','f'],['g','h','i']])
    >>> [['c', 'b', 'a'], ['f', 'e', 'd'], ['i', 'h', 'g']]

    horizontal_flip([['c', 'b', 'a'], ['f', 'e', 'd'], ['i', 'h', 'g']])
    >>> [['a','b','c'],['d','e','f'],['g','h','i']]
    '''

#   Create a deep copy to save the list's original composition.
    copy_list = deep_copy(list)

#   Iterate through each sublist in the list and assign each element to it's horizontal opposite.
    for sublist_index in range(len(list)):

        for char_index in range(len(list)):
            list[sublist_index][char_index] = copy_list[sublist_index][-1 - char_index]
        

def transpose(list):
    '''
    Takes the transpose of a matrix given in the form of a 2D list 
    
    (list) -> None
    transpose([['a','b','c'],['d','e','f'],['g','h','i']])
    >>> [['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f', 'i']]
    
    transpose([['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f', 'i']])
    >>> [['a','b','c'],['d','e','f'],['g','h','i']]

    transpose([['e', 'v', 'e'], [' ', 'y', 'r'], ['e', 'n', 'o']])
    >>> [['e', ' ', 'e'], ['v', 'y', 'n'], ['e', 'r', 'o']]
    '''

#   Creating a deep copy of the inputted list to save the origninal compostion.
    new_list = deep_copy(list)

#   Iterating through every list-sublist index and switching the indicies.
    for row in range(len(new_list)):
        for column in range(len(new_list)):
            list[row][column] = new_list[column][row]


def flip_list(list):
    '''
    Modifies an inputted 2D list by applying horizontal_flip() and then transpose()
    
    (list) -> None
    
    Examples:
    
    flip_list([['e', 'v', 'e'], [' ', 'y', 'r'], ['e', 'n', 'o']])
    >>> [['e', 'r', 'o'], ['v', 'y', 'n'], ['e', ' ', 'e']]

    flip_list([['e', 'r', 'o'], ['v', 'y', 'n'], ['e', ' ', 'e']])
    >>> [['o', 'n', 'e'], ['r', 'y', ' '], ['e', 'v', 'e']]

    flip_list([['a', 'c', 'T'], ['B', 'v', 'r'], ['u', 'u', 't']])
    >>> [['T', 'r', 't'], ['c', 'v', 'u'], ['a', 'B', 'u']]
    '''
   
    horizontal_flip(list)
    transpose(list)


def decipher_code(string):
    '''
    Takes a string, converts it to a list and decodes it, outputting the decoded string.
    A period indicates a separate statement to be decoded
    
    (str) -> str
    
    Examples:
    '''
#   Creating variables to be modified as the string is edited
    sentence_list = []
    last_edit = 0
    output_string = ""

#   Iterate through the length of the input string to find the end of sentences.
    for index in range(len(string)):

#       When the end of a sentence is located, separate the sentence and add it to a list.
        if string[index] == ".":
            sentence_list.append(string[last_edit:index])
            last_edit = index + 1

#       On the last iteration, add the final sentence even if no period is present.
        if index == len(string) - 1:
            sentence_list.append(string[last_edit:])

#   Modify each element and add it to the output string.
    for element in sentence_list:
        element_list = string2list(element)
        flip_list(element_list)
        output_string += list2string(element_list)

#       Separate the sentence with a period if it is not the last sentence in the message.
        if element != sentence_list[len(sentence_list) - 1]:
            output_string += "."

    return output_string
