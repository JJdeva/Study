def add_print_to(origin):
    def wrapper():
        print('start')
        origin()
        print('end')
    return wrapper

@add_print_to
def print_hello():
    print('Hello')
    
print_hello()