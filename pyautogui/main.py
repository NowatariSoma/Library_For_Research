from utils import FUDE

fude = FUDE()

for i in range(107,fude.n):
    print(i)
    fude.w_name(i)
    fude.w_kana(i)
    fude.w_address(i)
    fude.w_memo(i)
    fude.w_work(i)
    fude.w_mail(i)
    fude.w_phone(i)
    fude.w_address_2(i)
    fude.new_person()