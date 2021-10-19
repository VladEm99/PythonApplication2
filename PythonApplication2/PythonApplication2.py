ik=""
while len(ik)!=11 or ik.isdigit()!=True:
    try:
        ik=input("Введите свой личный код:   ")
    except ValueError:
        print("Введенный личный код - не правильный.\nВведите заново:   ")
    print("Анализ личного кода:".center(50,"-"))
    print("Первый символ:")
    ik_list=list(ik)
    if int(ik_list[0]) not in [1,2,3,4,5,6]:
        print(ik_list[0], "- не правильный!")
    else:
        print(ik_list[0]," - правильное число")
        kuu=ik_list[3]+ik_list[4] #1+0=10
        kuu=int(kuu)
    if kuu>0 and kuu<13:
        print(f"{ik_list[3]+ik_list[4]} - Правильные данные!")
    else:
        print(f"{ik_list[3]+ik_list[4]} - Не правильные данные!")
    paev=ik_list[5]+ik_list[6]
    paev=int(paev)
    if paev<1 or paev>31:
        print("Введены не правильные данные!")
    else:
        print(f"Введены правильные данные\n{ik_list[5]+ik_list[6]} - ваш день рождения.")
   
    if int(ik_list[0])==1 or int(ik_list[0])==2:
        aasta=int("18"+ik_list[1]+ik_list[2])
    elif int(ik_list[0])==3 or int(ik_list[0])==4:
        aasta=int("19"+ik_list[1]+ik_list[2])
    elif int(ik_list[0])==5 or int(ik_list[0])==6:
        aasta=int("20"+ik_list[1]+ik_list[2])
    print(aasta," - Ваш год рождения.")
if int(ik_list[0])==1 or int(ik_list[0])==3 or int(ik_list[0])==5:
    print("Ваш пол - мужской")
else:
    print("Ваш пол - женский")

Summa=0
for i in range(1, 11):
    if i<10:
        Summa+=i*int(ik_list[i-1])
    else:
        Summa+=(i-9)*int(ik_list[i-1])
print("Summa: ",Summa)
jaak=Summa//11
if jaak==10: #II astme kaal: 3 4 5 6 7 8 9 1 2 3
    Summa=0
    for i in range(3,13):
        if i<=9:
            Summa+=i*int(ik_list[i-1])
        else:
            Summa+=(i-9)*int(ik_list[i-1])
jaak=Summa//11
jaak=Summa-jaak*11
ikoodid=[]
arvud=[]
print("Kontrollnumber: ",jaak)
if jaak==int(ik_list[10]):
    print("Isikukood on õige!")
    ikoodid.append(ik)
else:
    print("Isikukood on vale!")
    arvud.append(ik)
print("Список правильных исикукодов -",ikoodid)
print("Список не правильных исикукодов -",arvud)
haig=ik_list[7]+ik_list[8]+ik_list[9]
print(haig)
new_list=list(haig)
print(new_list)
if int(haig) in range(1,11):
    print("kurressaare")
if int(haig) in range(11,20):
    print("tartu")
#год ik_list[1], ik_list[2]
#месяц ik_list[3], ik_list[4]
#день ik_list[5], ik_list[6]