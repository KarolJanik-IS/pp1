#17
import re
tekst = "To be, or not to be, that is the question"
samogloski = re.findall('[aeyioąęuó]',tekst)
print(f'liczba samogłosek w tekscie wynosi: {len(samogloski)}')