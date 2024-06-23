import time
import csv
def current_millisec_time():
    return round(time.time() *1000)

# sortare rapida:
def partitie(x, stanga, dreapta):
    pivot = x[dreapta]  
    i = stanga - 1 
    j = dreapta 
    while i < j:
        while True:
            i += 1
            if x[i] >= pivot:
                break
        while True:
            j -= 1
            if x[j] <= pivot:
                break
        if i < j:
            x[i], x[j] = x[j], x[i]
    x[i], x[dreapta] = x[dreapta], x[i]
    return i

def quicksort_crescator(x, stanga, dreapta):
    if stanga < dreapta:
        q = partitie(x, stanga, dreapta)
        x[stanga:q] = quicksort_crescator(x, stanga, q - 1)
        x[q + 1:dreapta + 1] = quicksort_crescator(x, q + 1, dreapta)
    return x[stanga:dreapta + 1]



with open("timp_quick_crescator2.csv","a",newline="") as f2:
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
        start_timp=current_millisec_time()
        n_comparatii=0
        n_mutari=0
        quicksort_crescator(l,0, len(l)-1)
        stop_timp=current_millisec_time()
        timp=stop_timp-start_timp
        with open("timp_quick_crescator2.csv","a") as f2:
            writer=csv.writer(f2)
            rezultat=[len(l),timp,n_comparatii,n_mutari]
            writer.writerow(rezultat)






