'''Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.'''

def string_rekurzija(string):
    #bazni slucaj
    if len(string)==0:
        return string
    #rekurzivni slucaj
    else:
        prvo_slovo=string[0]
        ostala_slova=string[1:]
        
        return string_rekurzija(ostala_slova) + prvo_slovo
    
rezultat=string_rekurzija("programiranje")
print(rezultat)
        
