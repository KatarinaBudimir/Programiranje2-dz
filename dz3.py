#Potrebno napisati regex koji vraca podudaranje
#ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
#a završava kao prvo slovo prezimena.
#String mora sadržavati bar jedan broj između 0 i 5 i razmak

import re
#regex="rijec koja počinje sa k ili K+broj, razmak, rijec koja zavrsava s b"
regex="^k|K([a-z]+)?[0-5]([a-z]+)?\s([a-z]+)?b$"

while 1:
    unos=input("Unesite string: ")
    rezultat=re.match(regex,unos)
    print(rezultat)
    if rezultat:
        break
    else:
        print("Nema podudaranja!")
print("Postoji podudaranje!")
