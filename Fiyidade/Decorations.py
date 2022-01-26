def mydecorator(function):
    
    def wrapper():
        print("Decoration")
        function()
    
    return wrapper

@mydecorator
def hello_world():
    print("Hello World")

hello_world()