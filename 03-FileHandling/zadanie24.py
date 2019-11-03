#24
tablica2D = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
with open('PlikTekstowy.csv','w') as file:
    file.write('Imie,Nazwisko,Email\n')
    for x in tablica2D:
        file.write(str(f"{x[0]},{x[1]},{x[2]}'\n'"))