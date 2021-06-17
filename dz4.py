#Napisati regex za provjeru validnosti unosa e-maila.
#E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
#Nakon toga napisati regex za provjeru eduId koji mora biti formata
#iprezimeX@sum.ba gdje je i prvo slovo imena + prezime.
#X predstavlja bilo koji broj (moze ici u beskonacnost),
#a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
#Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.



import re
ime=input("Unesite vase ime: ")
prezime=input("Unesite prezime: ")
#regex=ime.prezime@fpmoz.sum.ba
regex="^[a-z]+\.[a-z]+@fpmoz.sum.ba$"
#regex1=iprezime@sum.ba
#regex1="^[a-z]{1}[a-z]+([0-9]*)?@sum.ba$"
regex1="^" + ime[0] + prezime + "([0-9]*)?@sum.ba$"

while 1:
    unos=input("Unesite mail: ")
    unos1=input("Unesite eduId: ")
    rezultat=re.match(regex,unos)
    rezultat1=re.match(regex1,unos1)
    if rezultat and rezultat1:
        break
    else:
        print("Nepravilan unos!")
print("Uspješno ste unijeli mail i eduId!")
