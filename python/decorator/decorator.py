def print_hello():
    print('Hello')
    
def add_print_to(origin):
    def wrapper():
        print('start')
        origin()
        print('end')
    return wrapper

# add_print_to(print_hello)()

# hello = add_print_to(print_hello)
# hello()

print_hello