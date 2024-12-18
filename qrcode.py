import helper
import txtdata


class QRCode():
    '''
    Represents a QR Code.

    Attributes: last_update_date (str), owner (str), data (TxtData), error_correction (float).
    '''


    def __init__(self, file_path, last_update_date='00/00/0000', owner='Default Owner', error_correction=0.0):
        '''
        (str, str, str, num) -> None

        Initializes instance variables for QRCode Class.

        examples:
        
        >>> obj = QRCode('text.txt', 05/05/2005, 'Me', 0.0)
        >>> obj.owner
        Me

        >>> obj = QRCode('text.txt', 05/05/2005, 'Me', 0.0)
        >>> obj.error_correction
        0.0

        >>> obj = QRCode('text.txt', 05/05/2005, 'Me', 0.0)
        >>> obj.last_update_date['Day']
        05
        '''

        self.last_update_date = helper.convert_date(last_update_date)
        self.owner = owner
        self.data = txtdata.TxtData(helper.get_data(file_path))
        self.error_correction = error_correction


    def __str__(self):
        '''
        (None) -> str
        Returns a formatted string with info about the QR code

        examples:
        >>> obj = QRCode('text.txt', 05/05/2005, 'Me', 0.0)
        >>> print(obj)
        The QR code was created by Me and last updated in 2005.
        The details regarding the QR code file are as follows:
        This TxtData object has 6 rows and 18 columns.

        >>> obj = QRCode(file_path='text.txt', error_correction=0.4)
        >>> print(obj)
        The QR code was created by Default Owner and last updated in 0000.
        The details regarding the QR code file are as follows:
        This TxtData object has 6 rows and 18 columns.

        >>> obj = QRCode(file_path='not_text.txt', owner='The owner', error_correction=0.4)
        The QR code was created by The owner and last updated in 0000.
        The details regarding the QR code file are as follows:
        This TxtData object has 6 rows and 18 columns.
        '''

        self.rows = self.data.rows
        self.cols = self.data.cols
        return "The QR code was created by " + self.owner + " and last updated in " + self.last_update_date['Year'] + ".\nThe details " +\
        "regarding the QR code file are as follows:\nThis TxtData object has " + str(self.rows) + " rows and " + str(self.cols) + " columns."
    

    def equals(self, another_qrcode):
        '''
        (QRCode) -> bool

        Returns true if both TxtData data attributes are equal.

        examples:
        >>> qr_1 = QRCode('text.txt', 05/05/2005, 'Me', 0.0)
        >>> qr_2 = QRCode('text.txt', 05/05/2005, 'Me', 0.0)
        >>> qr_1.equals(qr_2)
        True

        >>> qr_1 = QRCode('text.txt', 05/12/2005, 'Not Me', 55)
        >>> qr_2 = QRCode('text.txt', 05/05/2005, 'Me', 0.0)
        >>> qr_1.equals(qr_2)
        True

        >>> qr_1 = QRCode('not_text.txt', 05/05/2005, 'Me', 0.0)
        >>> qr_2 = QRCode('text.txt', 05/05/2005, 'Me', 2322)
        >>> qr_1.equals(qr_2)
        False
        '''

#       Check if the TxtData objects in the data attribues are equal, and if the error corrections are equal
        return self.data.equals(another_qrcode.data) and\
         self.error_correction == another_qrcode.error_correction
    

    def is_corrupted(self, precise_qrcode):
        '''
        (QRCode) -> bool

        Returns true if the QR Code is corrupted, meaning the data attribute \
        is not within the error correction of the precise QRCode.

        examples:
        >>> qr_1 = QRCode('text.txt', 05/05/2005, 'Me', 0.5)
        >>> qr_2 = QRCode('text.txt', 05/05/2005, 'Me', 66.4)
        >>> qr_1.is_corrupted(qr_2)
        False

        >>> qr_1 = QRCode('text.txt', 05/05/2005, 'Me', 0.2)
        >>> qr_2 = QRCode('not_text.txt', 05/05/2005, 'Me', 0.2)
        >>> qr_1.is_corrupted(qr_2)
        True

        >>> qr_1 = QRCode('text.txt', 05/05/2005, 'Me', 0.8)
        >>> qr_2 = QRCode('Almost_text.txt', 05/05/2005, 'Me', 0.2)
        >>> qr_1.is_corrupted(qr_2)
        False
        '''

        return not(self.data.approximately_equals(precise_qrcode.data, self.error_correction))

        
