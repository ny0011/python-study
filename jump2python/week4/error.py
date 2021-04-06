class MyError(Exception):
    def __str__(self):
        return "Not Valid Nickname"

def say_nick(nick):
    if nick == "foo":
        raise MyError()
    print(nick)

try:
    say_nick("bar")
    say_nick("foo")
except MyError as e:
    print(f"ERROR: {e}")