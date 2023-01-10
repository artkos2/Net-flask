from flask import jsonify


class ApiError(Exception):

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

    def __repr__(self):
        return f"code\t{self.status_code}\nmessage\t{self.message}"

    def __str__(self):
        return self.__repr__()

