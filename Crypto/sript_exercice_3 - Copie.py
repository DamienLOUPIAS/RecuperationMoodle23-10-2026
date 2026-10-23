# Script de recherche des fréquences des lettres dans un texte

# Création d'un dictionnaire de la forme clé->valeur
# La clé sera une lettre entre A et Z, la valeur est le nombre d'occurrences de cette lettre dans le texte
# ---- Initialisation du dictionnaire avec une boucle
effectifs = {}
for i in range(65, 91): # Parcours des entiers de 65 à 90
    effectifs[chr(i)] = 0 # chr(i) renvoie le caractère dont le code ascii est i
# ---- Autre manière de faire : initialisation du dictionnaire avec une compréhension de dictionnaire
effectifs = {caractere : 0 for caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

# Ouverture du fichier à analyser et récupération du texte dans la variable le_texte
# Utilisation d'un contexte manager (syntaxe with ... open)
with open("TP2_Texte_Exercice2.txt", "r", encoding="utf8") as le_fichier:
    le_texte = le_fichier.read()
print(le_texte)

# Gestion des caractères accentués : à, â, é, è, ê, î, ï, ô, ù
le_texte=le_texte.replace("à", "a").replace("â", "a").replace("é", "e").replace("è", "e").replace("ê", "e")
le_texte=le_texte.replace("î", "i").replace("ï", "i").replace("ô", "o").replace("ù", "u").replace("û", "u")
le_texte=le_texte.replace("ç", "c")

# analyse du texte
caracteres_non_comptes = set() # ensemble des caractères non reconnus
for c in le_texte: # on parcourt le texte, caractère par caractère
    caractere = c.upper() # on bascule en majuscule
    if ord(caractere) >= 65 and ord(caractere) <= 90: # dans ce cas, on a une lettre entre A et Z
        effectifs[caractere] += 1 # on incrémente le nombre d'occurrences
    else:
        caracteres_non_comptes.add(c)

# détermination des fréquences
frequence = {} # dictionnaire qui contiendra les fréquences
# on cherche le nombre total de lettres
effectif_total = 0
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    effectif_total += effectifs[c]
# calcul des fréquences
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    frequence[c] = int(10000 * effectifs[c] / effectif_total) / 100

print(f"\n\n Les effectifs sont : {effectifs}\n\n")
print(f"\n\n Les fréquences sont : {frequence}\n\n")
print(f"\n\n Les caractères non reconnus sont :{caracteres_non_comptes}\n")

# production d'un diagramme des fréquences
import matplotlib.pyplot as plt
plt.bar(frequence.keys(), frequence.values())
plt.title("Fréquences d'apparition des caractères dans le texte")
plt.show()