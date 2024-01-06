# import sys

# def print_args(args):
#     if args:
#         print("Hello ", args)

# if __name__ == '__main__':
#     args = sys.argv[1]
#     print_args(args)

class HelloWorld():
    def __init__(self, name) -> None:
        self.name = name

    def greet(self, id: int):
        return "Hello " + self.name + " with id: " + str(id)