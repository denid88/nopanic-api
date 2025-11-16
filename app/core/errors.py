from enum import Enum

class ErrorCode(str, Enum):
    """error codes API"""
    # Authentication
    INVALID_EMAIL_OR_PASSWORD = "INVALID_EMAIL_OR_PASSWORD"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_ALREADY_EXISTS = "USER_ALREADY_EXISTS"
    UNAUTHORIZED = "UNAUTHORIZED"

    # Internal Server Error
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"