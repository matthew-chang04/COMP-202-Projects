STRING_SIZE_LIMIT = 1000
MIN_STRING_SIZE = 1

def deep_copy(list):
    new_list = []
    for sublist in list:
        new_sublist = []
        for char in sublist:
            new_sublist.append(char)
        new_list.append(sublist)
    return new_list


def check_square(string):
    for index in range(len(string)):
        if index ** 2 == len(string):
            return index
    return 0
    
def is_not_valid(string):

    for character in string:    
        if character < "A" or character > "z" and character != " ":
            return True

    return False

def is_not_square(string):

    return not(check_square(string))
            

def string2list(string):

    temp_list = []
    if is_not_valid(string) or is_not_square(string) or MIN_STRING_SIZE > len(string) or len(string) > STRING_SIZE_LIMIT:
        return temp_list
    
    for index in string:
        temp_list.append(index)
    
    sublist_len = check_square(string)
    list = [0] * sublist_len

    for index in range(len(list)):

        list[index] = temp_list[index * sublist_len: (index * sublist_len) + sublist_len]

    return list

def add_space(input_text):
    
    last_edit = 0
    string_copy = input_text
    output_text = ""
    for index in range(1,len(input_text) -1):

        if input_text[index] != input_text[index].lower() and input_text[index - 1].lower() == input_text[index - 1] and input_text[index + 1].lower() == input_text[index + 1] and input_text[index + 1] != " " and input_text[index - 1] != " ":
            output_text = output_text + string_copy[last_edit:index] + " "
            last_edit = index
        elif index == len(input_text) - 2:
            output_text += string_copy[last_edit:]


    return output_text
    
def list2string(list):

    string_result = ""

    for sublist in list:
        for char in sublist:
            string_result += char
    
    return add_space(string_result)

def horizontal_flip(list):

    for sublist in list:
        sublist = sublist[::-1]

"""
def transpose(list):
    
    new_list = deep_copy(list)

    for row in range(0, len(list)):
        for column in range(0, len(list)):
            list[row][column] = new_list[column][row]

"""
def flip_list(list):
    list = transpose(horizontal_flip(list))


def transpose(list):

    new_list = []
    
    for row in range(0, len(list)):
        new_sublist = []
        for column in range(0, len(list)):
            new_sublist.append(list[column][row])
        new_list.append(new_sublist)

    return new_list

list = [["a",'b','c'],['d','e','f'],['g','h','i']]

print(transpose(list))

print(list)
