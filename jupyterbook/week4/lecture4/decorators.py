
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
        pass
    return wrapper_do_twice
