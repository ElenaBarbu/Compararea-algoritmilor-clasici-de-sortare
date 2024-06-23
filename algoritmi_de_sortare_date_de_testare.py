##################### Crearea fisierului care contine datele de testare################################################




def aproape_sortata(lst,nr_elemente):
    # functie pentru crearea listelor aproape sortate
    #nr_elemente- numarul de elemente in lista


    elemente_sortate=[]
    elemente_nesortate=[]
    nr_elemente_sortate = int(0.9 * nr_elemente) # pentru a avea 90% din elemente sortate


    for i in range(0,nr_elemente_sortate):
      elemente_sortate.append(lst[i])  # partea listei care contine elementele sortate


    for i in range(nr_elemente_sortate, nr_elemente):
      elemente_nesortate.append(lst[i])
    random.shuffle(elemente_nesortate)  # pentru a pune in ordine aleatoare elementele pe care nu vrem sa le sortam

    # impreunarea partii cu elemente sortate cu partea cu elemente nesortate
    l_aproape_sortata= elemente_sortate + elemente_nesortate

    return l_aproape_sortata


import random
nr_elemente=int(input("Numarul de elemente: "))
l=[]
l_crescator=[]
l_aproape_crescator=[]
l_descrescator=[]
l_aproape_descrescator=[]

with open("date_testare.txt",'a') as f:
   
  for i in range(0,nr_elemente):
    numar=random.randrange(1,500000)
    l.append(numar)
   # Lista aleatoare
  #print("Lista cu numere aleatoare: ", l)
  linie=" ".join(map(str, l))    
  f.write(linie)
  f.write(" \n")

  # lista sortata crescator
  l_crescator=l.copy()
  l_crescator.sort()
  linie=" ".join(map(str, l_crescator))    
  f.write(linie)
  f.write(" \n")
  #print("Lista sortata crescator: ", l_crescator)

  #lista sortata descrescator
  l_descrescator=l_crescator.copy()
  l_descrescator.reverse()
  #print("Lista sortata descrescator: ",l_descrescator)
  linie=" ".join(map(str, l_descrescator))    
  f.write(linie)
  f.write(" \n")

  # lista 90% sortata crescator
  l_aproape_crescator=aproape_sortata(l_crescator,nr_elemente)
  #print("Lista aproape sortata crescator: ", l_aproape_crescator)
  linie=" ".join(map(str, l_aproape_crescator))    
  f.write(linie)
  f.write(" \n")

 
  # lista 90% sortata descrescator
  l_aproape_descrescator=aproape_sortata(l_descrescator,nr_elemente)
  #print("Lista aproape sortata descrescator: ", l_aproape_descrescator)
  linie=" ".join(map(str, l_aproape_descrescator))    
  f.write(linie)
  f.write(" \n")


""" lst=[]
lst1=[]
with open("date_testare.txt") as f2:
  for line in f2:
    lst=line.split(" ")
    for element in lst:
      if element!="\n":
        element=int(element)
        lst1.append(element)

print(lst1) """
