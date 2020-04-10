import sys

MESSAGE_LIST = []

def authorise(function):
    def wrapper(*args, **kwargs):
        auth_token = ''
        if len(sys.argv) == 2:
            auth_token = sys.argv[1]
        if not authorised(auth_token):
            raise ValueError("Invalid authentication")
        else:
            return function(*args, **kwargs)
    return wrapper

def authorised(auth_token):
    return auth_token == "CrocodileLikesStrawberries"

@authorise
def get_messages():
    return MESSAGE_LIST

@authorise
def add_messages(msg):
    global MESSAGE_LIST
    MESSAGE_LIST.append(msg)

if __name__ == '__main__':

    add_messages("Hello")
    add_messages("How")
    add_messages("Are")
    add_messages("You?")
    print(get_messages())
