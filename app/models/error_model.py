class PostError(Exception):
    def __init__(self, message, status, *args, **kwargs):
        super().__init__(message, status, *args, **kwargs)

        self.message = {"msg": message}
        self.status = status