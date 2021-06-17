'''Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
Jedna od funkcija neka bude definirana lambda izrazom, a druga standardnim načinom.
Zatim definiraj treću funkciju koja kao parametar prima naziv funkcije za ispis dobrodošlice
i poziva je tako što pošalje vaše ime u nju.
Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije.'''

ime=str(input("Unesite ime: "))

def funkcija_pozdrav(ime):
    pozdrav=print("Pozdrav "+ ime +"!")
    return pozdrav
#funkcija_pozdrav(ime)



funkcija_dobrodosao=lambda ime: print("Dobrodošao " + ime + "!")
funkcija_dobrodosao(ime)



def funk3(funkcija):
    funkcija(ime)
  
funk3(funkcija_pozdrav)
#funk3(funkcija_dobrodosao)





