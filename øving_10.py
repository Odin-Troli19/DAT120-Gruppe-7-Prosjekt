
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


#G
class Sted:
    def __init__(self, id, navn, adresse):
        self.id = id
        self.navn = navn
        self.adresse = adresse

    def __str__(self):
        return f"Id: {self.id}, Navn: {self.navn}, Adresse: {self.adresse}"

#H
def nytt_sted():
    id = input("Oppgi id:")
    navn = input("Skriv inn navnet:")
    adresse = input("Skriv inn gateadresse, postnummer og poststed:")
    return Sted(id, navn, adresse)

print(nytt_sted())



#I
def lagre_lese_sted():
    s = open("test_fil.txt", "r+")
    print(s.readline())
    s.close()
    return s

#J      
def skrivUt_sted(liste, overskrift=""):
    print(overskrift)
    indeks = 1
    for sted in liste:
        print(f"{indeks}: {sted}")
        indeks += 1

#K
class avtale_2:
  def __init__(self, tittel, sted, start, varighet,kategori):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
    self.kategori = kategori
    
    
def legg_til_kategori():
    ny_kategori = None
    print("Skriv en ny kategori til systemet(id, navn, prioritet i tall(1 til 3)): ")
    kategori_id = input("Skriv in ID: ")
    kategori_navn = input("Skriv in navnet: ")
    kategori_prioritet = int(input("Skriv in prioritet (som tall, 1 til 3): "))
    ny_kategori = kategori(kategori_id,kategori_navn,kategori_prioritet)
    
    ny_kategori = avtale_2()
    return ny_kategori

#L
def lagrer_kategori_sted():
    liste = list()
    tekstfil = open("avtalene.txt", "w")
    for avtale in liste:
        tekstfil.write(f"{avtale.tittel};{avtale.sted};{avtale.start};{avtale.varighet};{kategori.kategori};{sted.sted}\n")
    tekstfil.close()
  
liste = list()   
def leserinnavtale(liste):
    with open('avtalene.txt', 'r') as fp:
        for line in fp:
            splittet = line.strip().split(";")
            a = Avtale(splittet[4], splittet[3], splittet[0], splittet[1],splittet[2])

            liste.append(a)

#M
def menu ():
    min_liste = list()
   
    while True:
        print("[1] Lese inn avtale.")
        print("[2] Skrive inn avtale til fil.")
        print("[3] Skrive inn ny avtale")
        print("[4] Skrive ut alle avtaler.")
        print("[5] Endre en avtale.")
        print("[6] Slett avtale.")
        print("[7] Legg til kategorier.")
        print("[8] Legg en kategori til avtalen.")
        print("[9] Finne avtaler som foregår et bestemt sted .")
        print("[10] Avslutte programmet")
    
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
            endre_avtale_2(min_liste[indeks])
        elif option == 6:
            slett_avtale(min_liste)
        elif option == 7:
            print("Du har valgt alternativ 7 - Legg til kategorier.")
            legg_til_kategori(min_liste)
            lagrer_kategori_sted(min_liste)
        elif option == 8:
            legg_kategori_til_avtalen(min_liste)
        elif option == 9:
            finne_alle_avtaler_på_et_sted(min_liste)
        elif option == 10:
            print("Du har valgt alternativ 4 - (Avslutte programemt)")
            break
        

def slett_avtale_2(liste):
    indeksenTil = int(input("Hvilke indeksen til lisa vil du slette ? ")) -1

    liste.pop(indeksenTil)

def endre_avtale_2(Avtale):
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

    menu()
        
    
#N
def nytt_sted(): 
    ny_stedet = None
    while not ny_stedet:
        try:
            ID = input("Angi ID : ")
            navn = input("Angi navn : ")
            a = input("Angi gateadresse ")
            b = int(input("Angi postnummer"))
            c = input("Angi poststed ")
            adresse = a+b+c
            ny_stedet = sted(ID,navn,adresse)
        except Exception as error:
                    print(error)
    return ny_stedet
    
#O
def legg_kategori_til_avtalen():
    print("hello")
   
   
#P
min_liste = list()
def finne_alle_avtaler_på_et_sted():
    a = input("hvilket sted søker du etter? ")
    if a in min_liste:
        filter_objekt = filter(lambda a: 'sted:' in a, min_liste)
        print(list(filter_objekt))
    else:
        print('Det finnes ikke !')
        
#Q
def __str__(self):
  return f"tittel: {self.tittel}, Sted: {self.sted}, starttidspunkt: {self.start}, Varighet: {self.varighet}min, kategori:{kategori.kategori}, sted: {sted.sted} "
    
   
