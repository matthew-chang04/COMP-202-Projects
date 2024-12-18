import helper
import copy


class TxtData():
    '''
    Represents the data within a file as a list

    Attributes: data (list), rows (int), cols (int)
    '''

    def __init__(self, data):
        '''
        Initializes the TxtData object.
        
        (list) -> None
        
        examples:
        >>> obj = TxtData([1,1,0],[1,1,0],[1,1,0],[1,1,0],)
        >>> obj.rows
        4

        >>> obj = TxtData([1,1,1],[1,1,1])
        >>> obj.cols
        3

        >>> obj = TxtData([1,1,1])
        >>> obj.data
        [1,1,1]
        '''

        self.data = copy.deepcopy(data)
        self.rows = len(data)
        self.cols = len(data[0])


    def __str__(self):
        '''
        (None) -> str

        Returns a formatted string with information about the TxtData object.

        examples:
        >>> obj = TxtData([1,1,1])
        >>> print(obj)
        This TxtData object has 1 rows and 3 columns.

        >>> obj = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> print(obj)
        This TxtData object has 3 rows and 4 columns.

        >>> obj = TxtData([1,0],[1,0],[1,0],)
        >>> print(obj)
        This TxtData object has 3 rows and 2 columns.
        '''

        return f'This TxtData object has {self.rows} rows and {self.cols} columns.'
        
    
    def get_pixels(self):
        '''
        (None) -> num

        Returns the number of entries in a TxtData object.

        examples:
        >>> obj = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj.get_pixels()
        12

        >>> obj = TxtData([1,0],[1,0],[1,0],)
        >>> obj.get_pixels()
        6

        >>> obj = TxtData([1,1,1])
        >>> obj.get_pixels()
        3
        '''

        return self.rows * self.cols
    

    def get_data_at(self, row, col):
        '''
        (num, num) -> num

        Returns the data found in the specified row and column

        >>> obj = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj.get_data_at(1,1)
        1

        >>> obj = TxtData([1,0],[1,0],[1,0],)
        >>> obj.get_data_at(0,2)
        Traceback: most recent call last
        ValueError: Index out of bound!

        >>> obj = TxtData([1,1,1])
        >>> obj.get_data_at(1,2)
        1
        '''
        
        if row >= self.rows or col >= self.cols:
            raise ValueError('Index out of bound!')
        
        return self.data[row][col]
    

    def pretty_save(self, file_name):
        '''
        (str) -> None
        Creates a QR code in the file name specified
        
        Examples:
        >>> obj = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj.pretty_save('pretty_file.txt')
        >>> file = open('pretty_file.txt', 'r')
        >>> print(file.read())
        \u2588\u2588  \u2588\u2588  
        \u2588\u2588  \u2588\u2588  
        \u2588\u2588  \u2588\u2588  

        >>> obj = TxtData([1,0,1,0])
        >>> obj.pretty_save('pretty_file.txt')
        >>> file = open('pretty_file.txt', 'r')
        >>> print(file.read())
        \u2588\u2588  \u2588\u2588  

        >>> obj = TxtData([1,1,1])
        >>> obj.pretty_save('pretty_file.txt')
        >>> file = open('pretty_file.txt', 'r')
        >>> print(file.read())
        \u2588\u2588\u2588\u2588\u2588\u2588
        '''

        new_file = open(file_name, 'w')

        for sublist in self.data:
            line_str = ''
            for char in sublist:
                if char == 0:
                    line_str += '  '
                elif char == 1:
                    line_str += '\u2588\u2588'
            new_file.write(line_str + '\n')
        
        new_file.close()

    def equals(self, another_data):
        '''
        (TxtData) -> bool
        Returns true if both TxtData instances have the same data attribute.

        >>> obj1 = TxtData([1,0,1,0])
        >>> obj2 = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj1.equals(obj2)
        False

        >>> obj1 = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj2 = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj1.equals(obj2)
        True

        >>> obj1 = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj2 = TxtData([1,0,0,1,0,1])
        >>> obj2.equals(obj1)
        False
        '''

        return self.data == another_data.data
    
      
    def approximately_equals(self, another_data, precision):
        '''
        (TxtData, float) -> bool
        Returns true if the rate of inconsistent entries is less than the precision variable.

        Examples:
        >>> obj1 = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj2 = TxtData([0,0,0,0],[1,0,0,0],[1,0,0,0])
        >>> obj1.approximately_equals(obj2, 0.1)
        False

        >>> obj1 = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj2 = TxtData([1,0,1,0],[1,0,1,0],[1,0,1,0])
        >>> obj1.approximately_equals(obj2, 0.4545)
        True

        >>> obj1 = TxtData([1,0,0,0,0,1], [1,0,0,0,0,1], [1,0,0,0,0,1])
        >>> obj2 = TxtData([1,0,0,0,0,1], [1,0,1,0,0,1], [1,0,0,0,0,1])
        >>> obj1.approximately_equals(obj2, 0.9)
        True
        '''

#       Initialize count for inconsistent values.
        sublist_count = 0
        inconsistent_num = 0

        for sublist in another_data.data:
            char_count = 0
            for char in sublist:
#               When inconsisten values are found, add to the count
                if char != self.data[sublist_count][char_count]:
                    inconsistent_num += 1
                char_count += 1
            sublist_count += 1

#       Find inconsistent rate.
        inconsistent_rate = inconsistent_num / self.get_pixels()
        
        return precision >= inconsistent_rate
    
