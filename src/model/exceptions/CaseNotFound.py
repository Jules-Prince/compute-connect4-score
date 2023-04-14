class CaseNotFound(Exception):
    def __init__(self, x, y):
        super().__init__("Case not found at {", x, ";", y, "}")