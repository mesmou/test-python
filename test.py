#!/usr/bin/python3
import sys
print(sys.version_info)
print(sys.version)
print(sys.platform)
valeur = "toto"
if valeur == "cat":
    print("ok")
elif valeur == "dog":
    print("dog ok")
else:
    print("inconnu")
i = 5
mykey = "temps"
fois = 20
print('la valeur %d et le mot \'%s\' apparaissent %d fois,' % (i, mykey, fois))
print('la valeur {} et le mot \'{}\' appraissent {} fois'.format(i, mykey, fois))
seq = [1,2,3,4]
m,n,g,d = seq
print (m)
for letter in "spam" :
    print ("current letter", letter)
    fruits=['banane', 'pomme', 'mangue']
for fruit in fruits:
    print("mon fruit", fruit)
# on a deux variables temps et distance
temps= 9.896
distance= 19.7
vitesse =  distance/temps
print('la vitesse est de  {} m/s'.format(vitesse))
a = 9
print("le carré de {} est {}".format(a, a**2))
# en utilisant la fonction range
# afficher les entiers de 0 à 3
a = range(10)
b= list(a)
print(b)
print(b[:4])
print(b[4:8])
#avec une boucle afficher les caractères suivantes
for i in range(10):
    if i > 3:
        print("...", i)
        if i==7:
            break



liste = [17,38,10,25,72]
#triez et afficher la liste
liste.sort()
print(liste)
# ajouter l'élément 12
liste.append(12)
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)

