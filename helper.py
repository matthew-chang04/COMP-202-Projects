     
def convert_date(date_str):
    '''
    (str) -> dict
    Takes a date string in format 'dd/mm/yyyy' and returns a dictionary with keys 'Day', 'Month', 'Year'
    
    examples:
    >>> convert_date(123123123)
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    
    >>> convert_date(04/05/2024)
    {'Day': 04, 'Month': 05, 'Year': 2024}

    >>> convert_date(0405202455)
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    '''

    key_list = ['Day', 'Month', 'Year']
    date_dict = {}

#   Verify that the input string is of the correct format
    if len(date_str) != 10 or date_str[2] != '/' or date_str[5] != '/':
        raise ValueError('Input format incorrect!')

#   Create a list to modify from the input string    
    date_list = date_str.split('/')

#   Iterate through key and value list to create dictionary
    key_count = 0
    for element in date_list:
        date_dict[key_list[key_count]] = element
        key_count += 1

    return date_dict

def get_data(file_path):
    '''
    (str) -> list
    Takes a file path string and returns a 2D list of the lines within it.
    
    examples:
    
    >>> get_data('QRcode.txt')
    [[1,0,1,0,0],[1,0,1,0,0],[1,0,1,0,0],[1,0,1,0,0],[1,0,1,0,0],]

    >>> get_data('invalid.txt')
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!

    >>> get_data('small.txt')
    [[1,0], [0,1]]
    '''

    file = open(file_path, 'r')

#   Create a 2d list based on the lines in the file.  
    entry_list = []
    for line in file:
        sublist = []
        for char in line:
            if char == '0' or char == '1':
                sublist.append(int(char))
            elif char != '\n':
                raise ValueError('File should contain only 0s and 1s!')
        entry_list.append(sublist)

    file.close()
    return entry_list


    
