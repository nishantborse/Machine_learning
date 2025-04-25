#write custom exception classes
import sys #functions and va that are used to manipulate the Python runtime environment
import os

def error_handling(error, error_details:sys):
    _,_,_exc_tb=error_details.exc_info() #exc_info() returns a tuple of three values: the exception type, the exception value, and the traceback object.
    file_name=_exc_tb.tb_frame.f_code.co_filename   #tb_frame is the current stack frame, and f_code.co_filename is the name of the file that contains the code being executed.
    error_message="Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, _exc_tb.tb_lineno, str(error)) #tb_lineno is the line number where the exception occurred.
    return error_message #returning the error message


class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message) #calling the parent class constructor
        self.error_message=error_handling(error_message, error_details=error_details)
    def __str__(self):
        return self.error_message   #string representation of the object, which is the error message.
    
"""if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e, sys) #raising the custom exception with the error message and error details.
        """