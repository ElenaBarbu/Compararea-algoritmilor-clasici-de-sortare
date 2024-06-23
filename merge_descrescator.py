import time
import csv
def merge_descrescator(stanga, dreapta):
    rezultat_interclasare = []
    index_jumatatea_stanga = 0
    index_jumatatea_dreapta = 0

    while index_jumatatea_stanga < len(stanga) and index_jumatatea_dreapta < len(dreapta):
        if stanga[index_jumatatea_stanga] >= dreapta[index_jumatatea_dreapta]:
            rezultat_interclasare.append(stanga[index_jumatatea_stanga])
            index_jumatatea_stanga += 1
        else:
            rezultat_interclasare.append(dreapta[index_jumatatea_dreapta])
            index_jumatatea_dreapta += 1
    while index_jumatatea_stanga<len(stanga):
      rezultat_interclasare.append(stanga[index_jumatatea_stanga])
      index_jumatatea_stanga +=1
    while index_jumatatea_dreapta<len(dreapta):
      rezultat_interclasare.append(dreapta[index_jumatatea_dreapta])
      index_jumatatea_dreapta +=1

    return rezultat_interclasare
def merge_sort_descrescator(l):
    if len(l) <= 1:
        return l
    else:
      m = len(l) // 2
      jumatatea_stanga = l[:m]
      jumatatea_dreapta = l[m:]

      # recursivitate
      jumatatea_stanga = merge_sort_descrescator(jumatatea_stanga)
      jumatatea_dreapta = merge_sort_descrescator(jumatatea_dreapta)

      # Merge
      return merge_descrescator(jumatatea_stanga,jumatatea_dreapta)
    
# sortare descrescatoare prin interclasare:
with open("timp_merge_descrescator.csv","a",newline="") as f2:
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
        merge_sort_descrescator(l)
        stop_timp=time.time()
        timp=stop_timp-start_timp
        with open("timp_merge_descrescator.csv","a") as f2:
            writer=csv.writer(f2)
            rezultat=[len(l),timp,n_comparatii,n_mutari]
            writer.writerow(rezultat)






