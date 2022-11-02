# -*- coding: utf-8 -*-
"""
Prosjektoppgave: Enkel avtalebok 
Dere skal implementere en enkel tekstbasert avtalebok, inkludert mulighet
 for å lagre avtalelista til fil 
og hente den fra fil. Avtaleboka skal kunne registrere avtaler med tittel,
 sted, start-tidspunkt og 
varighet 
"""

import datetime as dt



class Avtale:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = x
    self.varighet = varighet
    
    
  def __str__(self):
    return f"tittel: {self.tittel}, Sted: {self.sted}, starttidspunkt: {self.start}, Varighet: {self.varighet}min" 

A1 = Avtale("Møte", "Stavanger", "placeholder", 30)

print(A1)

A2 = Avtale("Fotball", "Drammen", "placeholder", 90)
print(A2)





x = dt.datetime.now()

class Avtale:
    def __init__(self, tittel, sted, start, varighet):
      self.tittel = tittel
      self.sted = sted
      self.start = x
      self.varighet = varighet
      
      
    def __str__(self):
        return f"tittel: {self.tittel}, Sted: {self.sted}, starttidspunkt: {self.start}, Varighet: {self.varighet}min"



    def __repr__(self):
        return f"tittel: {self.tittel}, Sted: {self.sted}, starttidspunkt: {self.start}, Varighet: {self.varighet}min"
      
      
def avtale_funksjon(ordliste, overskrift=""):
    #print(ordliste)
    print(overskrift)
    for avtale in ordliste:
        print(avtale)
      
avtaler_liste = list()

A1 = Avtale("Møte", "Stavanger", "placeholder", 30)

print(A1)

A2 = Avtale("Fotball", "Drammen", "placeholder", 90)
print(A2)


avtaler_liste.append(A1)
avtaler_liste.append(A2)



avtale_funksjon(avtaler_liste)
avtale_funksjon(avtaler_liste, "Denne gangen med overskrift")


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
    
     
a=ny_avtale()
print(a)
# A1 = Avtale("Møte", "Stavanger", "placeholder", 30)

# print(A1)

# A2 = Avtale("Fotball", "Drammen", "placeholder", 90)
# print(A2)
