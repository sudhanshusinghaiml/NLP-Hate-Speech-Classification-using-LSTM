import os
import sys

def get_error_message_detail(error_message, message_detail: sys):
    _, _, exec_tb = message_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(file_name, exec_tb.tb_lineno, str(error_message))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, message_detail):
        """
        
        :param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = get_error_message_detail(
            error_message= error_message,
            message_detail= message_detail
        )

    def __str__(self):
        return self.error_message