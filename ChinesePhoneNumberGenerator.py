import random


def get_phone_number() -> str:
    phone_code_list = [
        '137',
        '138',
        '184',
        '176',
        '177',
        '178',
        '147',
        '132',
        '133',
        '157',
        '131',
        '187',
        '181',
        '136',
        '153',
        '186',
        '183',
        '134',
        '180',
        '189',
        '185',
        '159',
        '145',
        '156',
        '188',
        '151',
        '182',
        '158',
        '170',
        '135',
        '139',
        '150',
        '155',
        '130',
        '152']
    return random.sample(phone_code_list, 1)[0] + \
        str(random.randint(0, 99999999)).zfill(8)


if __name__ == '__main__':
    print(get_phone_number())
