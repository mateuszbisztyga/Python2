from enum import Enum

class Timetable:
    
    def __init__(self, nazwaPrzystanku, godzinaOdjazdu):
        self.nazwaPrzystanku = nazwaPrzystanku
        self.godzinaOdjazdu = godzinaOdjazdu

    def ZwrocGodzineOdjazdu(self):
        return self.godzinaOdjazdu


class Bus:

    def __init__(self, numerLini):
        self.numerLini = numerLini


class Passanger:

    def __init__(self, typBiletu):
        self.typBiletu = typBiletu


class Ticket:

    def __init__(self, podstawowaCena):
        self.podstawowaCena = podstawowaCena


    def CenaBiletuDla(self, typBiletu):
        if(typBiletu == TicketType.Normalny):
            return self.podstawowaCena
        if(typBiletu == TicketType.Ulgowy):
            return self.podstawowaCena - self.podstawowaCena * 0.20
        
class TicketType(Enum):
    Normalny = 1 # Cena 100% podstawy
    Ulgowy = 2   # Cena  80% podstawy


def GodzinaOdjazduDla(numerLini, nazwaPrzystanku):
    if(numerLini == 1):
        if(nazwaPrzystanku == "Krzyki"):
            return Linia1Krzyki.godzinaOdjazdu
        if(nazwaPrzystanku == "PsiePole"):
            return Linia1PsiePole.godzinaOdjazdu
    if(numerLini == 2):
        if(nazwaPrzystanku == "Krzyki"):
            return Linia2Krzyki.godzinaOdjazdu
        if(nazwaPrzystanku == "PsiePole"):
            return Linia2PsiePole.godzinaOdjazdu
        if(nazwaPrzystanku == "Tarnogaj"):
            return Linia2Tarnogaj.godzinaOdjazdu
    



Linia1Krzyki = Timetable("Krzyki", "[20:39]")
Linia1PsiePole = Timetable("PsiePole", "[20:37]")

Linia2Krzyki = Timetable("Krzyki", "[21:39]")
Linia2PsiePole = Timetable("PsiePole", "[21:37]")
Linia2Tarnogaj = Timetable("Tarnogaj", "[21:49]")


busSupertest = Bus(1) # bus nr lini 1
busSuper2 = Bus(2) # bus nr lini 2

print(GodzinaOdjazduDla(busSupertest.numerLini, "PsiePole"))




ticket = Ticket(20) # Podstawowa cena
passanger = Passanger(TicketType.Ulgowy)

print(ticket.CenaBiletuDla(passanger.typBiletu))