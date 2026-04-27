
class DataQualityError(Exception):
    """
    Base class for all custom exceptions in the data quality engine.
    """
    pass 

class InvalidFileFormatError(DataQualityError):
    """
    Raise when the file format is not supported.

    Example: expecting .csv but recieved .txt
    """
    pass 

class EmptyDatasetError(DataQualityError):
    """
    Raised when dataset is empty after loading.
    """
    pass 

class DataParsingError(DataQualityError):
    """
    Raised when file parsing fails due to malformed structure or invalid content.
    """
    pass 