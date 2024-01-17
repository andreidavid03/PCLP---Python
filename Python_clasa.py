
#determin ce date retin
    #citesc fisier  pe linii
    #lucrez doar pe liniile care contin date de interes
    #salvez acele date pentru ficare punct

#scriu datele intr-un fiser csv
    #scriu capul de tabel
    #punct,MZ,FY
    #pe cate un rand nou, scriu:
    #pct,val_mz, val_fy


puncte = ['N_', 'NE', 'E_', 'ES', 'S_', 'SW', 'W_', 'WN', 'N_']
FY = []
MZ = []

for pct in puncte:
    fisier = "SECT_C150_" + pct + ".txt"
    f = open(fisier,'r')
    continut = f.readlines()
    f.close()
    for rand in continut:
        #validez rand si salvez date necesare (MZ, FY)
        lista_rand = rand.split()
        if len(lista_rand) == 3 and lista_rand[0] == "FY":
           FY.append(lista_rand[2])
        if len(lista_rand) == 3 and lista_rand[0] == "MZ":
           MZ.append(lista_rand[2])

f_rez = open("centralizare.csv","w")
#f_rez.write("punct,MZ,FY\n")
print("punct,MZ,FY",file = f_rez)
for i in range(len(puncte)):
    #f_rez.write(puncte[i] + "," + MZ[i] + "," + FY[i] + "\n")
    print(puncte[i] + "," + MZ[i] + "," + FY[i], file = f_rez)
f_rez.close()

