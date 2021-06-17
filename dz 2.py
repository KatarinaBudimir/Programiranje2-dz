from csv import reader
# open file in read mode
with open('C:/Users/User/Desktop/Programiranje 2/ntorke/rezultati.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    lista_ntorki = list(map(tuple, csv_reader))
    # display all rows of csv
    #for rezultat in lista_ntorki:
    #    if int(rezultat[2]) > 49:
    #        print(rezultat)

    def vratiPrezime(ntorka):
        return ntorka[1]

    lista_ntorki.sort(key=vratiPrezime)  
    
    for rezultat in lista_ntorki:
        print(rezultat)

    ocjene={
        'Nedovoljan 0-49%': 0,
        'Dovoljan 50-64%': 0, 
        'Dobar 65-79%': 0, 
        'Vrlodobar 80-89%': 0, 
        'Izvrstan 90-100%': 0, 
        }

    for rezultat in lista_ntorki:
        if int(rezultat[2]) < 50:
            ocjene['Nedovoljan 0-49%'] += 1
        elif int(rezultat[2]) < 65:
            ocjene['Dovoljan 50-64%'] += 1
        elif int(rezultat[2]) < 80:
            ocjene['Dobar 65-79%'] += 1
        elif int(rezultat[2]) < 90:
            ocjene['Vrlodobar 80-89%'] += 1
        else:
            ocjene['Izvrstan 90-100%'] += 1

    print("\n\n")

    for oc in ocjene:
        print(oc,"-",ocjene[oc])





            
    
