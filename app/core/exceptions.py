class BusinessException(Exception):
    """
    Base class for all business logic errors in the application.
    
    Attributes:
        name (str): A short, unique error code (e.g., "USER_NOT_FOUND").
        reason (str): A human-readable message explaining the error.
    """
    def __init__(self, name: str, reason: str):
        self.name = name
        self.reason = reason