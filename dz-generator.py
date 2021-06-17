#Napraviti generator funkcije za ispis svih parnih
#i svih neparnih brojeva manjih od prosljeđenog parametra.

def parni(proslj_param):
    broj=2

    while broj<proslj_param:
        yield broj
        broj+=2
print("Parni brojevi manji od prosljeđenog parametra: ")    
for i in parni(10):
    print(i)

print("\n\n")

def neparni(proslj_param):
    broj=1

    while broj<proslj_param:
        yield broj
        broj+=2

print("Neparni brojevi manji od prosljeđenog parametra: ")
for i in neparni(10):
    print(i)

