import time
import csv
# sortare crescatoare prin insertie:
with open("timp_bubble_crescator.csv","a",newline="") as f2:
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
        for i in range((len(l)-1),0,-1):
            for j in range(0,i):
                n_comparatii+=1
                if l[j]>l[j+1]:
                    n_mutari+=1
                    aux=l[j]
                    l[j]=l[j+1]
                    l[j+1]=aux       

        stop_timp=time.time()
        timp=stop_timp-start_timp
        with open("timp_bubble_crescator.csv","a") as f2:
            writer=csv.writer(f2)
            rezultat=[len(l),timp,n_comparatii,n_mutari]
            writer.writerow(rezultat)






