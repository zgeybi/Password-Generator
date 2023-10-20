import random


class Chars:
    def shuffle(self, templist):
        random.shuffle(templist)
        return ''.join(templist)

    def get_chars(self, func, res, n=4):
        res = []

        def wrapper():
            for i in range(n):
                func(res)
            return res
        return wrapper

    def get_lowercase(self, list_):
        list_.append(chr(random.randint(97, 122)))

    def get_digits(self, list_):
        list_.append(chr(random.randint(48, 57)))

    def get_uppercase(self, list_):
        list_.append(chr(random.randint(65, 90)))

    def get_punctuation(self, list_):
        list_.append(chr(random.choice([random.randint(33, 47), random.randint(58, 64)])))


# Main program starts here
def generator():
    chars = Chars()
    mylist = []
    punctuation = chars.get_chars(chars.get_punctuation, mylist)
    uppercase = chars.get_chars(chars.get_uppercase, mylist)
    lowercase = chars.get_chars(chars.get_lowercase, mylist)
    digits = chars.get_chars(chars.get_digits, mylist)

    punctuation = punctuation()
    uppercase = uppercase()
    lowercase = lowercase()
    digits = digits()

    password = punctuation + uppercase + lowercase + digits
    password = chars.shuffle(password)
    return password

