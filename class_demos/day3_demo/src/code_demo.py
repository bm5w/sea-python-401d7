# counter = 0


# def count_up():
#     # counter += 1
#     counter = counter + 1


foo = 'bar'

def build_name(last='Hunt-Walker', first='Nick'):
    print('{} {}'.format(first, last))


def pets(count, animal='cat'):
    print('I have {count} {animal}s'.format(count=count, animal=animal))


# def numbers(one, two, *args, buckle='my shoe', **kwargs):
#     """This does a thing with some stuff."""
#     print(args)
#     print(kwargs)
#     for num in args:
#         print(num)


# def profile(username, password, **settings):
#     user = User()
#     user.username = username
#     user.password = password
#     for setting in settings:
#         user.config[setting] = settings[setting]


# # 5!
# # 5 * 4 * 3 * 2 * 1
# # 6 * 5 * 4 * 3 * 2 * 1

def factorial(num):
    """Calculate the factorial of the provided number."""
    if num < 0:
        raise ValueError('Cannot take a number less than zero.')
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


def factorial_loop(num):
    """Calculate the factorial of the provided number iteratively."""
    if num < 0:
        raise ValueError('Cannot take a number less than zero.')
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


def guess_num(num):
    if num < 10:
        return 'Yay!'
    elif num >= 20:
        return 'Double boo!'
    elif num >= 10:
        return 'Boo!'
    else:
        return 'This will never actually run'


def car(radio=None):
    if radio:
        return 'Play 106.5'
    return 'Silence'
    # print('Play 106.5') if radio else print('Silence') # <-- ternary operator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

# for letter in letters:
#     print(letter)

# for i in range(len(letters)):
#     print(letters[i])

for idx, item in enumerate(letters):
    letters[idx] = item.upper()

numbers = []
for i in range(1, 101):
    numbers.append(i)

[num for num in range(1, 101)]  # <-- list comprehension

# [do_something(letter) for letter in letters]

if __name__ == "__main__":
    # if this code is run from the command line, do stuff
    print('Nathan has small hands')