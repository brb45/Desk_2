## custom exception
# 1.
class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Incorrect value of {value}"
        super().__init__(message)

val = 9999
if val  > 100:
    raise IncorrectValueError(val)

#     raise IncorrectValueError(val)
# __main__.IncorrectValueError: Incorrect value of 9999

# 2.from class GitHubApiException(Exception):
#
class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__(message)


