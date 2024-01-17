#dictionar - {punct: MZ, FY}

def citeste_fisier(den_fisier):
    #ce am de facut
    f = open(den_fisier,'r')
    continut = f.readlines()
    f.close()
    return continut


def adunare(a,b,c):
    if a>b:
        return a+c
    if a>c:
        return a+b
    return 0
    
print(adunare(1,4,6) + 5)
print(adunare(6,4,5) + 5)


puncte = {"Puncte":["FY","MZ"],
          'N_':[], 'NE':[], 'E_':[], 'ES':[],
          'S_':[], 'SW':[], 'W_':[], 'WN':[]}

for pct in puncte.keys():
    if pct == "Puncte":
        continue
    fisier = "SECT_C150_" + pct + ".txt"

    continut = citeste_fisier(fisier)
    
    for rand in continut:
        #validez rand si salvez date necesare (MZ, FY)
        lista_rand = rand.split()
        if len(lista_rand) == 3 and lista_rand[0] == "FY":
           puncte[pct].append(lista_rand[2])
        if len(lista_rand) == 3 and lista_rand[0] == "MZ":
           puncte[pct].append(lista_rand[2])
with open ('centralizare_rez.csv','w') as f_rez:
    for k,v in puncte.items():
        print (k + "," + ",".join(v),file = f_rez)
    print ("N_," + ",".join(puncte["N_"]), file = f_rez)


