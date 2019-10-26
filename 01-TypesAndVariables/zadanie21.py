#21. Napisz program, który dla podanej wartości temperatury wyrażonej w stopniach Celsjusza odczytanej z klawiatury wyznaczy temperaturę w stopniach Fahrenheita oraz Kelvina.
celciusz = float(input())
fahrenheit = (celciusz * 1.8) + 32
kelvin = celciusz +  273.15
print(celciusz,"stopni celcjusza to ", fahrenheit, "stopni fahrenheita lub ", kelvin, "kelwinów")

