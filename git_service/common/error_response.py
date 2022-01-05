""" Error response preparation"""


class ErrorResponseVo:
    """Error Response vo"""

    def __init__(self):
        self.error = None


class ErrorResponse:
    """Error Response"""

    def __init__(self):
        self.statusCode = None
        self.name = None
        self.message = None


def error_response_preparation(status_code, name, msg):
    """method to prepare error response"""
    error_response_vo = ErrorResponseVo()
    error_response = ErrorResponse()
    error_response.statusCode = status_code
    error_response.name = name
    error_response.message = str(msg)
    error_response_vo.error = error_response.__dict__
    return error_response_vo.__dict__
