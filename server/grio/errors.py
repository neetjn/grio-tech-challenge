class PersonNotFoundError(Exception):
    status_code = 404
    message = "Person not found"


class PersonConflictError(Exception):
    status_code = 409
    message = "An error has occurred"
