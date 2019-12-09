#7

class Student():
    licznikNumerowAlbumu = 100000
    uczelnia = "UEK Kraków"
    def __init__(self,imie,nazwisko,kierunekStudiow):
        self.imie = imie
        self.nazwisko = nazwisko
        Student.licznikNumerowAlbumu += 1
        self.nrAlbumu = Student.licznikNumerowAlbumu
        self.kierunekStudiow = kierunekStudiow
    def __str__(self):
        return f'{self.imie} ({self.nrAlbumu}), {self.kierunekStudiow}, {Student.uczelnia}'
student1 = Student("Wacław","POTOCKI","Informatyka stosowana")
print(student1)
student2 = Student("Wacław","POTOCKI","Informatyka stosowana")
student3 = Student("Wacław","POTOCKI","Informatyka stosowana")
print(student2)
print(student3)