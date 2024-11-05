STRING_SIZE_LIMIT = 1000
MIN_STRING_SIZE = 1

def check_square(string):
    for index in range(len(string)):
        if index ** 2 == len(string):
            return index
    return 0
    
def is_not_valid(string):

    for character in string:
        if character.isdecimal():
            return True
    
    return False

def is_not_square(string):

    return not(check_square(string))
            

def string2list(string):

    temp_list = []
    if is_not_valid(string) or is_not_square(string) or MIN_STRING_SIZE > len(string) or len(string) > STRING_SIZE_LIMIT:
        return temp_list
    
    for index in string:
        temp_list += index
    
    sublist_len = check_square(string)
    list = [0] * sublist_len

    for index in range(len(list)):

        list[index] = temp_list[index * sublist_len: index * sublist_len + sublist_len]

    return list

def add_space(input_text):

    output_text = ""
    for index in range(1,len(input_text)-2):

        if input_text[index - 1].lower() == input_text[index - 1] and input_text[index + 1].lower() == input_text[index + 1] and input_text[index] != input_text[index].lower():
            replacement = input_text[:index]

            output_text += (replacement + " ")

    return output_text

print(add_space("HelloMyNameIs"))



