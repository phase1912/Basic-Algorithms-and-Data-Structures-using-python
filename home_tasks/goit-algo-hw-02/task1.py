import re
import uuid
from queue import Queue
from typing import Callable

class Request:
    def __init__ (self, data: str = "some data"):
        self.id = uuid.uuid4()
        self.data = data

    def __str__(self):
        return f"id: {self.id}, data: {self.data}"

class RequestHandler:
    def __init__(self, queue: Queue):
        self.queue = queue

    def generate_request(self, data: str = "some data"):
        request = Request(data)
        self.queue.put(request)

    def process_request(self):
        if not self.queue.empty():
            request = self.queue.get()
            return request
        else:
            return None

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if re.match(r"not enough|too many", e.args[0]):
                return "Incorrect number of arguments"
            elif e.args:
                return str(e)
            else:
                return "Incorrect value!"
        except Exception as e:
            return f"{e}" if e.args else "Oops! Something went wrong..."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def create_request_command(args, request_handler: RequestHandler):
    if len(args) == 0:
        raise ValueError("Invalid count of arguments.")

    data, = args

    request_handler.generate_request(data)

    return "Request added."

@input_error
def process_request_command(request_handler: RequestHandler):
    return request_handler.process_request()

def main():
    queue = Queue()
    requestHandler = RequestHandler(queue)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "create_request":
            print(create_request_command(args, requestHandler))
        elif command == "process_request":
            result = process_request_command(requestHandler)

            if result is None:
                print("Empty queue")
            else:
                print(result)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

