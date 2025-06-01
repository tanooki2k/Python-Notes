# EXAMPLE N1:
def greet():
    friend = yield
    print(f'Hello, {friend}')


g = greet()
g.send(None)  # priming the generator
g.send('Adam')


# EXAMPLE N2:
from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jenn', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting}, {friend}')


def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
