import string
import random


def get_email(num=None) -> list:
    m = []
    char_list = ''.join(
        [string.digits, string.ascii_letters, string.punctuation])
    i = 0
    if num:
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
    else:
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
        return p


if __name__ == '__main__':
    print(get_email(5))
