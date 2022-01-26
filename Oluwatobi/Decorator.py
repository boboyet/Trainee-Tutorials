from curses import wrapper


def mydeco(function):

    def wrapper():
        print("I am decorating my function")
        function()

    return wrapper

@mydeco
def hello_world():
        print("Hello Jesse")

hello_world()