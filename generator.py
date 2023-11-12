import random


def shuffle(templist):
    random.shuffle(templist)
    return ''.join(templist)


def get_chars(func, res, n=4):
    res = []

    def wrapper():
        for i in range(n):
            func(res)
        return res
    return wrapper


def get_lowercase(list_):
    list_.append(chr(random.randint(97, 122)))


def get_digits(list_):
    list_.append(chr(random.randint(48, 57)))


def get_uppercase(list_):
    list_.append(chr(random.randint(65, 90)))


def get_punctuation(list_):
    list_.append(chr(random.choice([random.randint(33, 47), random.randint(58, 64)])))


# Main program starts here

def generator():
    """
        generates random 16-char password and returns it
        :return: 16-char randomly generated string
    """
    mylist = []
    punctuation = get_chars(get_punctuation, mylist)
    uppercase = get_chars(get_uppercase, mylist)
    lowercase = get_chars(get_lowercase, mylist)
    digits = get_chars(get_digits, mylist)

    punctuation = punctuation()
    uppercase = uppercase()
    lowercase = lowercase()
    digits = digits()

    password = punctuation + uppercase + lowercase + digits
    password = shuffle(password)
    return password
