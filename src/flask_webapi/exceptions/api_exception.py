class ApiException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super(ApiException, self).__init__(message)
