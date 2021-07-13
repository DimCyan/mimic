import ChinaAddressGenerator
import ChineseNameGenerator
import ChinesePhoneNumberGenerator
import ChineseIDCardNumberGenerator
import ChineseBankCardNumberGenerator
import EmailGenerator


class Pleco(object):
    def address(self):
        return ChinaAddressGenerator.get_china_address()

    def name(self):
        return ChineseNameGenerator.get_chinese_name()

    def phone(self):
        return ChinesePhoneNumberGenerator.get_phone_number()

    def idnum(self):
        return ChineseIDCardNumberGenerator.get_id()

    def banknum(self):
        return ChineseBankCardNumberGenerator.get_bank_card()

    def email(self):
        return EmailGenerator.get_email()
if __name__ == '__main__':
    p = Pleco()
    print(p.address())
    print(p.name())
    print(p.phone())
    print(p.idnum())
    print(p.banknum())
    print(p.email())
