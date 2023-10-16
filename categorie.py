#Programme qui calcule le prix TTC d’un produit connaissant son prix hors taxe et sa catégorie.
a=0.7
b=0.2
c=0.25
tva=0
ttc=0
cat=input("Choisisez la categorie (A,B,C) : ")
ph=float(input("Entrer le prix hors taxe :"))
if(cat=="A" or cat=="a"):
    tva=ph*a
    ttc=ph+tva
elif(cat=="B" or cat=="b"):
    tva=ph*b
    ttc=ph+tva
elif(cat=="B" or cat=="b"):
    tva=ph*c
    ttc=ph+tva
else:
    print("Veuillez entrer la categorie qui est disponible")
print(f"Le prix en TTC est : {ttc} Dh")

    