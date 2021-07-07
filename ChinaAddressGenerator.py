from utils import ChineseChars, ChinaCityName
import random


def get_china_address() -> str:
    return '{}{}路{}号{}栋{}室'.format(
        ChinaCityName.get_city_name(), ChineseChars.get_chinese_chars(
            random.randint(
                2, 3)), random.randint(
            1, 200), random.randint(
                    1, 99), random.randint(
                        101, 9999))


if __name__ == '__main__':
    print(get_china_address())
