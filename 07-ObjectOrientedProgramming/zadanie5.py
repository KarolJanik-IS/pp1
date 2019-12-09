#5
class ut():
    def __init__(self,wykonawca,utwor,album,rok):
        self.wykonawca = wykonawca
        self.utwor = utwor
        self.album = album
        self.rok = rok
    def __str__(self):
        return f'{"Wykonawca:":10}  {self.wykonawca}' + "\n" + f'{"Utwór:":10}  {self.utwor}' + "\n" + f'{"Album:":10}  {self.album}' + "\n" + f'{"Rok:":10}  {self.rok}'
nieMaFal = ut("Dawid Podsiadło","Nie ma fal","Małomiasteczkowy","2018")
print(nieMaFal)