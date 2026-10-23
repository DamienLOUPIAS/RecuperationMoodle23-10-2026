# définition de l'alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# création d'un dictionnaire pour passer d'un caractère de l'alphabet à sa classe
caractereToClasse = {caractere : classe for caractere, classe in zip(alphabet, range(0, len(alphabet)))}

# fonction permettant d'appliquer une transformation affine sur les caractères d'un texte
# Elle peut chiffrer ou déchiffrer
def appliqueTransformationAffine(texteClair, modulo, cle):
    texteChiffre = ""
    a, b = cle
    for caractere in texteClair:
        texteChiffre += alphabet[(caractereToClasse[caractere] * a + b) % modulo]
    return(texteChiffre)

print(appliqueTransformationAffine("JUYWPUTGUPYIWYUZIYDGCG", len(alphabet), (19, 2)))