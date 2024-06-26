import logging
import time
from time import sleep

import logging
import time
from functools import wraps

def log(level):
    def decorator_log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            if callable(func):
                logging.log(level, f"Called function {func.__name__} with arguments {args, kwargs}. "
                                   f"Execution time: {duration} seconds. "
                                   f"Return value: {result}.")
            return result
        return wrapper

    def decorator_log_class(cls):
        orig_init = cls.__init__
        @wraps(cls.__init__)
        def new_init(self, *args, **kwargs):
            start_time = time.time()
            orig_init(self, *args, **kwargs)            
            end_time = time.time()
            duration = end_time - start_time
            
            logging.log(level, f"Instantiated class {cls.__name__} with arguments {args, kwargs}." f"Execution time: {duration} seconds. ")
        cls.__init__ = new_init
        return cls

    def final_decorator(arg):
        if isinstance(arg, type):
            return decorator_log_class(arg)
        else:
            return decorator_log(arg)

    return final_decorator
    
@log(logging.INFO)
def hey():
    print("Hey!")
    sleep(1)
    
@log(logging.DEBUG)
def print_num(num: int):
    print(num)
    return ((num / 2) ** (132/321)) ** 124

@log(logging.INFO)
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    hey()
    print_num(12)
    
    human = Human("John", 23)
    