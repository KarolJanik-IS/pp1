#24
tablicaImion = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy","Teofil"]
najdluzsze = ""
for x in tablicaImion:
    if len(najdluzsze) < len(x):
        najdluzsze = x
print(najdluzsze)