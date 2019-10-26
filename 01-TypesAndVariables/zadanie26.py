#35. Napisz program obliczający wskaźnik masy ciała BMI (ang. Body Mass Index) na podstawie podanego wzrostu w cm oraz masy ciała w kg. Dane użytkownik wprowadza z klawiatury. Formułę wyznaczającą wskaźnik BMI odszukaj w sieci Internet. Następnie, korzystając z programu, sprawdź, czy posiadasz prawidłową wagę. Pamiętaj o utworzeniu w pierwszej kolejności algorytmu rozwiązania przy użyciu komentarzy.
wzrost = float(input("Podaj wzrost w cm: "))
wzrost = wzrost/100 #Zamieniam cm na metry
waga = float(input("Podaj wagę w kg: "))
bmi = waga/(wzrost*wzrost)
print("Wskaźnik BMI:",bmi)


#Nie do końca rozumiem co oznacza sformułowanie:   "Pamiętaj o utworzeniu w pierwszej kolejności algorytmu rozwiązania przy użyciu komentarzy"
