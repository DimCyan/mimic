import random
from utils import ChineseChars, ChineseLastName


def get_chinese_name(first_name_sum=None) -> str:
    if first_name_sum:
        return ChineseLastName.get_last_name() + ChineseChars.get_chinese_chars(first_name_sum)
    else:
        return ChineseLastName.get_last_name(
        ) + ChineseChars.get_chinese_chars(random.randint(1, 2))


if __name__ == '__main__':
    print(get_chinese_name())
