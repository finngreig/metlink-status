class ServiceUpdateList:
    def __init__(self, rows):
        self.rows = rows

    def get_rows(self, user_service=None):
        if user_service:
            return [service for service in self.rows if service.is_service_affected(user_service)]
        else:
            return self.rows

    def is_empty(self):
        return len(self.rows) == 0
