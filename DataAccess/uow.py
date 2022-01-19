

class UOW:
    """
    Unit of work pattern it is a gateway to fetch data access classes for providers layer
    """
    def __init__(self, cursor):
        self.__cursor = cursor

    def get_event_detection_data_access(self):
        return EventDetectionDataAccess(self.__cursor)
