class ClientException(Exception):
    resp_status = 400
    message = ""

    def __init__(self, message="Произошла непредвиденная ошибка", resp_status=400):
        self.resp_status = resp_status
        self.message = message
        super().__init__(message)


class ServerException(Exception):
    resp_status = 500
    message = ""

    def __init__(self, message="Произошла непредвиденная ошибка", resp_status=500):
        self.resp_status = resp_status
        self.message = message
        super().__init__(message)
