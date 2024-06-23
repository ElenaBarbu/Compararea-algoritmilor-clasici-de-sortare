import time
import csv
# sortare crescatoare prin insertie:
with open("timp_selectie_descrescator2.csv","a",newline="") as f2:
    writer=csv.writer(f2)
    header=["Nr. el.","Timp","Comp.","mutari"]
    writer.writerow(header)

with open("date_testare.txt","r") as f2:
    for line in f2:
        lst=[]
        l=[]
        lst=line.split(" ")
        for element in lst:
            if element!="\n":
                element=int(element)
                l.append(element) # l este lista cu elemntele de pe linie
        start_timp=time.time()
        n_comparatii=0
        n_mutari=0
        for i in range(0,(len(l)-1)):
            i_max=i
            for j in range((i+1),len(l)):
                n_comparatii+=1
                if l[j]>l[i_max]:
                    i_max=j
            if i_max != i :
                n_mutari+=1
                aux=l[i]
                l[i]=l[i_max]
                l[i_max]=aux
        stop_timp=time.time()
        timp=stop_timp-start_timp
        with open("timp_selectie_descrescator2.csv","a") as f2:
            writer=csv.writer(f2)
            rezultat=[len(l),timp,n_comparatii,n_mutari]
            writer.writerow(rezultat)






