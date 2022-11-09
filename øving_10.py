
import datetime as dt

#d
class Avtale:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
    
#e    
  def __str__(self):
    return f"tittel: {self.tittel}, Sted: {self.sted}, starttidspunkt: {self.start}, Varighet: {self.varighet}min" 

#f
def ny_avtale():
    Avtalen = None
    while not Avtalen:
        try:        
            tittel_1 = input("Angi tittel til avtalen : ")
            sted_1 = input("Angi stedet til avtalen : ")
            start_tidspunkt_1 = input("Angi dato og tidspunkt på formatet: dd:mm:yyyy tt:mm ")
            start_tidspunktdaytime = dt.datetime.strptime(start_tidspunkt_1, "%d:%m:%Y %H:%M")
            varighet_1 = int(input("Angi varighte i minutter :"))
            Avtalen=Avtale(tittel_1, sted_1, start_tidspunktdaytime, varighet_1)
        except Exception as error:
                print(error)
    return Avtalen
    
     

#g      
def avtale_funksjon(liste, overskrift=""):
    print(overskrift)
    indeks = 1
    for avtale in liste:
        print(f"{indeks}: {avtale}")
        indeks += 1
      
# avtaler_liste = list()

# A1 = Avtale("Møte", "Stavanger", "placeholder", 30)



# A2 = Avtale("Fotball", "Drammen", "placeholder", 90)



# avtaler_liste.append(A1)
# avtaler_liste.append(A2)



#avtale_funksjon(avtaler_liste)
# avtale_funksjon(avtaler_liste, "Avtaler")


#h

def setteLista_ifile(liste):
    tekstfil = open("avtalene.txt", "w")
    for avtale in liste:
        tekstfil.write(f"{avtale.tittel};{avtale.sted};{avtale.start};{avtale.varighet}\n")
    tekstfil.close()
#i
# printUtlista = []

def åpnefilen(liste):
# åpne filen og les innholdet i en liste
    with open('avtalene.txt', 'r') as fp:
        for line in fp:
        # fjerne linebreak fra et nåværende navn
        # linebreak er det siste tegnet i hver linje
            splittet = line.strip().split(";")
            a = Avtale(splittet[0], splittet[1], splittet[2], splittet[3])

        # legge til gjeldende element i listen
            liste.append(a)

#j
import pandas as pd 


def is_dato(date_string):
    try:
        pd.to_datetime(date_string, format='%d.%m.%Y')
        return True
    except Exception:
        return False
    
    x = ["test", "Stavanger","27.02.2020", "300" ]
    for index, item in enumerate(x):
        if is_dato(item):
           print(index)

#import pandas as pd 

# x = ["test", "Stavanger","27.02.2020", "300"]
def is_dato(date_string):
    try:
        pd.to_datetime(date_string, format='%d.%m.%Y')
        return True
    except Exception:
        return False
    
    x = ["test", "Stavanger","27.02.2020", "300" ]
    for index, item in enumerate(x):
        if is_dato(item):
           print(index)
        
        
        
#k
def avtalerogstreng(liste_avtaler, streng=""):
    retur_liste = list()
    for avtale in liste_avtaler:
        if streng in avtale.tittel:
            retur_liste.append(avtale)
    return retur_liste
   
   

        
#l
def menu ():
    min_liste = list()

    
    while True:
        print("[1] Lese inn avtale.")
        print("[2] Skrive inn avtale til fil.")
        print("[3] Skrive inn ny avtale")
        print("[4] Skrive ut alle avtaler.")
        print("[5] Endre en avtale.")
        print("[6] Slett avtale.")
        print("[9] Avslutte programmet")
    
        print("Du må ta valgene til venstre for å velge et alternativ")


        option = int(input("Skriv inn ditt alternatv:"))
        if option == 1:
            print("Du har valgt alternativ 1 - (Lese inn avtale)")
            åpnefilen(min_liste)
        elif option == 2:
            print("Du har valgt alternativ 2 - (Skrive inn avtale til fil)")
            setteLista_ifile(min_liste)
        elif option == 3:
            print("Du har vlagt alternativ 3 - (Skrive inn ny avtale)")
            min_liste.append(ny_avtale())
        elif option == 4:
            avtale_funksjon(min_liste, "hallo")
        elif option == 5:
            indeks = int(input("hvilken avtale vil dere endre?")) - 1
            endre_avtale(min_liste[indeks])
        elif option == 6:
            slett_avtale(min_liste)
        elif option == 9:
            print("Du har valgt alternativ 4 - (Avslutte programemt)")
            break
        

# print()
# menu()
# option = int(input("Skriv inn ditt alternativ"))

#M
def slett_avtale(liste):
    indeksenTil = int(input("Hvilke indeksen til lisa vil du slette ? ")) -1

    liste.pop(indeksenTil)





#N
#import datetime as dt

def endre_avtale(Avtale):
    print("Hvilken nøkkel vil du endre")

    valg = input("Skriv inn nøkkelen du vil endre:")
    if valg.lower() == "tittel":
        ny_tittel = input("skriv inn ny tittel")
        Avtale.tittel = ny_tittel

    elif valg.lower() == "sted":
        nytt_sted = input("Skriv nye stedet")
        Avtale.sted = nytt_sted
    
    elif valg.lower() == "starttidspunkt":
        start_tidspunkt_1 = input("Angi dato og tidspunt på formatet. dd:mm:yyyy tt:mm")
        nytt_starttidspunkt = dt.datetime.strptime(start_tidspunkt_1, "%d:%m:%Y %H:%M")
        Avtale.start = nytt_starttidspunkt

    elif valg.lower() == "varighet":
        ny_varighet = int(input("angi den nye varigheten"))
        Avtale.varighet = ny_varighet
    else: 
        print("Det du satt inn stemte ikke, prøv på nytt.")


if __name__=="__main__":
    # listeAvtaler = list()
    # a1 = Avtale("hei", "oslo", dt.datetime.fromisoformat("2022-11-12 12:00:00"), 30)
    # a2 = Avtale("hei", "oslo", dt.datetime.fromisoformat("2022-11-12 12:00:00"), 30)
    # listeAvtaler.append(a1)
    # listeAvtaler.append(a2)
    # tom_liste = list()
    # åpnefilen(tom_liste)
    # avtale_funksjon(tom_liste, "hallo")
    menu()
    
# menu()





#ØVING 10!!!!


#C
class Kategori:
    def __init__(self, tid, navn, prioritet=1):
        self.tid=tid
        self.navn=navn
        self.prioritet=prioritet
        
        
    def __str__(self):
        return f"tid: {self.tid}, Navn: {self.navn}, Prioritet: {self.prioritet}" 
    
#D
def ny_kategori():
    tid=input("Skriv inn tiden: ")
    navn=input("Skriv inn navn: ")
    prioritet=input("Skriv inn prioriteten til kategorien: ")
    return Kategori(tid, navn, prioritet)



#E Lagrer 
def Kategori_i_fil(liste):
    tekstfil = open("kategorier.txt", "w")
    for kategori in liste:
        tekstfil.write(f"{kategori.tid};{kategori.navn};{kategori.prioritet}\n")
    tekstfil.close()
    
#E Leser inn
def åpnefilen(liste):
# åpne filen og les innholdet i en liste
    with open('kategorier.txt', 'r') as fp:
        for line in fp:
        # fjerne linebreak fra et nåværende navn
        # linebreak er det siste tegnet i hver linje
            splittet = line.strip().split(";")
            a = Kategori(splittet[0], splittet[1], splittet[2], splittet[3])

        # legge til gjeldende element i listen
            liste.append(a)
    

print(ny_kategori())

