#Koristeći listu imena iz prethodnog zadatka
#svakom studentu generirati nasumičnu ocjenu od 1 do 5.
#Prebrojati u rječnik koliko ima kojih ocjena.
#Izračunati postotak prolaznosti. (sve ocjene veće od 1)

import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael', 'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan', 'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan', 'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel', 'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario', 'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina', 'Josip', 'Lucija']

brojOcjena={
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5":0
    }
for ime in imena:
    ocjena=random.randint(1,5)
    print(ime,"-",ocjena)
    for oc in brojOcjena:
        if int(oc)==ocjena:
            brojOcjena[oc] += 1
            break
prolaznost= (len(imena) - brojOcjena["1"])/len(imena)

for oc in brojOcjena: 
    print(oc,brojOcjena[oc])

print("Prolaznost je: ",prolaznost*100 , "%")
