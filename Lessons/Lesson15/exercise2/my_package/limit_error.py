class LimitError(Exception):

    def __init__(self, message = "In the group cannot be more than 10 students"):
        self.message = message
        super().__init__(self.message)
