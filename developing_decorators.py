from functools import wraps
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="decorators.log",
    format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%x-%X",
)

def log_timestamp(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        logging.info(func.__name__)
        result = func(*args, **kwargs)
        return result
    return _wrapper

@log_timestamp
def spam(count):
    print(f"Hello from spam() {count}")
    return "abc"
# spam = log_timestamp(spam) 

def ham():
    print("Hello from ham()")
    return "def"
ham = log_timestamp(ham)

spam(27)
ham()
print(spam.__name__, ham.__name__)
