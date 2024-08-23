indeks = {
    "Celcius   ": "c",
    "Reamur    ": "r",
    "Fahrenheit": "f",
    "Kelvin    ": "k"
}
print("========= Indeks Satuan Skala Suhu =========")
for i in indeks:
    print("Satuan suhu :", i, "\t Indeks :", indeks[i])

suhu = float(input("Masukkan Suhu : "))
satuan = input("Masukkan indeks satuan skala suhu : ")

if (satuan == "c"):
    print(suhu, "derajat celcius :")
    print("Reamur = ", (suhu * 4 / 5), "derajat")
    print("Fahrenheit = ", (suhu * 9 / 5) + 32, "derajat")
    print("Kelvin = ", suhu + 273, "derajat")
elif (satuan == "r"):
    print(suhu, "derajat reamur :")
    print("Celcius = ", (suhu * 5 / 4), "derajat")
    print("Fahrenheit = ", (suhu * 9 / 4) + 32, "derajat")
    print("Kelvin = ", (suhu * 5 / 4) + 273, "derajat")
elif (satuan == "f"):
    print(suhu, "derajat fahrenheit :")
    print("Celcius = ", (5 / 9) * (suhu - 32), "derajat")
    print("Reamur = ", (4 / 9) * (suhu - 32), "derajat")
    print("Kelvin = ", (5 / 9) * (suhu - 32) + 273, "derajat")
elif (satuan == "k"):
    print(suhu, "derajat kelvin :")
    print("Celcius = ", suhu - 273, "derajat")
    print("Reamur = ", (4 / 5) * (suhu - 273), "derajat")
    print("Fahrenheit = ", (9 / 5) * (suhu - 273) + 32, "derajat")
