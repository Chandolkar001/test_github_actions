import sys

def print_message(args):
    message = " ".join(args)
    print(f"Received arguments: {message}")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    print_message(arguments)
