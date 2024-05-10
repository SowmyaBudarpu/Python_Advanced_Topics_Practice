#implementing the Singleton pattern in Python

'''The Singleton pattern is used to ensure that a class has only one instance and provides a global point of access to that instance'''


from threading import Lock

class A:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
