kilo = int (input("Kilonuzu Giriniz:"))
boy = int (input("Boyunuzu Giriniz(cm cinsinden):"))
boy = boy/100
indeks = kilo/(boy*boy)
print("Vücut Kitle İndex'iniz {}".format(round(indeks)))
print ("İndeks: ", indeks)


if  indeks <=18.5 :
    print("Zayıfsınız (•‿•)")
    print("{} kilogram almanız gerekiyor.".format(round(25*(boy*boy) -kilo)))
elif indeks< 25 :
    print("Bu kiloda kalmaya devam etmelisiniz +_+.")
elif indeks < 30:
    print("Fazla Kilolusunuz. >_<")
    print("{} kilogram vermeniz gerekiyor ".format(kilo- round(25*(boy*boy) )))
elif indeks < 35:
    print("1. derece obezsiniz O_o")
    print("{} kilogram vermeniz gerekiyor".format(kilo- round(25*(boy*boy) )))
elif indeks < 40:
    print("2. derece obezsiniz O_o")
    print("{} kilogram vermeniz gerekiyor".format(kilo- round(25*(boy*boy) )))
elif indeks < 45:
    print("3. derece obezsiniz O_o")
    print("{} kilogram vermeniz gerekiyor".format(kilo- round(25*(boy*boy) )))