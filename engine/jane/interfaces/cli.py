from ..engine import step


def main():
    print('triggered cli lol')
    while (True):
        user_input = input('You: ')
        jane_response = step(user_input)
        print('Jane: ' + jane_response)
