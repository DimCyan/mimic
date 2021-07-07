import string
import random


def get_email(num) -> list:
    m = []
    char_list = ''.join(
        [string.digits, string.ascii_letters, string.punctuation])
    i = 0
    while i < num:
        s = [
            '@163.com',
            '@qq.com',
            '@sina.com',
            '@126.com',
            '@msn.com',
            '@yahoo.com',
            '@gmail.com',
            '@hotmail.com']
        h = random.choice(s)
        rang = random.randint(6, 12)
        random_number = "".join(random.choice(char_list) for j in range(rang))
        p = "{}{}".format(random_number, h)
        if p not in m:
            m.append(p)
            i += 1
    return m


if __name__ == '__main__':
    print(get_email(5))
