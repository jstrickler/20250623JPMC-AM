import logging

logging.basicConfig(
    level=logging.INFO,
    filename="decorators.log",
    format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%x-%X",
)

def log_timestamp(func):
    def _wrapper():
        logging.info(func.__name__)
        result = func()
        return result
    return _wrapper

@log_timestamp
def spam():
    print("Hello from spam()")
    return "abc"
# spam = log_timestamp(spam) 

def ham():
    print("Hello from ham()")
    return "def"
ham = log_timestamp(ham)

spam()
ham()

