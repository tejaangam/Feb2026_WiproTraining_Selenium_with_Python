#decorator - wrapper function around the function are called decorators. They are used to modify the behavior of a function without changing its code.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def choclate_cake():
    print("I am a chocolate cake")

@make_pretty
def vanilla_cake():
    print("I am a vanilla cake")

vanilla_cake()
choclate_cake()