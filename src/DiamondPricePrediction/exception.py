import sys
class CustomException(Exception):

    def __init__(self, errorMsg, errorDetail:sys):
        self.errorMsg = errorMsg
        _,_,exc_tb = errorDetail.exc_info()
        self.lineNo = exc_tb.tb_lineno
        self.fileName = exc_tb.tb_frame.f_code.co_filename


        def __str__(self):
            return f"Error occured in python script name {self.fileName} line number {self.lineNo} error message {self.errorMsg}"