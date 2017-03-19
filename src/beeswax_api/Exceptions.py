class BeeswaxException(Exception):
    def __init__(self, response):
        self.body = response.json()
        self.status_code = response.status_code

    def __str__(self):
        return str(self.body)


class LoginException(BeeswaxException):
    pass


class SegmentUploadException(BeeswaxException):
    pass
