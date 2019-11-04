#27
import re
s = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
samogloski = ['a','e','y','i','o','ą','ę','u','ó']
#cyfry = re.findall('\d',line)
for x in samogloski:
    samogloska = re.findall(x,s)
    print(f'Samogłoska: {x} występuje: {len(samogloska)} razy, \t\t częstość {len(samogloska)}/{len(s)}')