import time
import csv
# sortare crescatoare prin insertie:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
 

with open("timp_quick2_crescator.csv","a",newline="") as f2:
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
        quicksort(l)
        stop_timp=time.time()
        timp=stop_timp-start_timp
        with open("timp_quick2_crescator.csv","a") as f2:
            writer=csv.writer(f2)
            rezultat=[len(l),timp,n_comparatii,n_mutari]
            writer.writerow(rezultat)
