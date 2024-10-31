strochka = input("Введите вашу строку: ")
all_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
gls = 0
sgls = 0
for i in strochka.lower() :
    if i in all_gls:
        gls += 1
    else:
        sgls +=1
print("Длина вашей строки равна: ", len(strochka))
print("Гласных в ней: ", gls)
print("Согласных в ней: ", sgls)

