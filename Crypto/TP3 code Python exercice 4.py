# script pour le chiffrement et le déchiffrement par Vigenère
# avec un alphabet à définir

# l'alphabet donné sous forme d'une chaine de caractère
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.!"
# dictionnaire pour passer d'un caractère à une classe
dico_caractere_classe = dict()
classe = 0
for caractere in alphabet :
    dico_caractere_classe[caractere] = classe 
    classe += 1
#print(dico_caractere_classe)

def vigenere(message, cle, code = True):
    """ Chiffrement d'un message avec le chiffre de Vigenère
    Args :
        message(str) : le message
        cle(str) : la clé secrète
        code(boolean) : chiffrement (si True) ou déchiffrement (si False)
    Returns : (str)
        le message chiffré ou déchiffré
    """
    le_texte = ""
    
    i = 0
    longueur_alphabet = len(alphabet)
    for c in message : # on passe en revue tous les caractères du message
        if code :
            le_texte = le_texte + alphabet[(dico_caractere_classe[cle[i]] + dico_caractere_classe[c]) % longueur_alphabet]
        else :
            le_texte = le_texte + alphabet[(-dico_caractere_classe[cle[i]] + dico_caractere_classe[c]) % longueur_alphabet]
        i += 1
        if i == len(cle): # on doit reparir du début de la clé
            i = 0

    return(le_texte)


# exemple de chiffrement et déchiffrement
print(vigenere("VOILA", "AB", True))
print(vigenere(vigenere("VOILA", "AB", True), "AB", False))
print(vigenere(vigenere("VOILA UN EXEMPLE AVEC UNE CLE !!!", "ICI C EST LA CLE", True), "ICI C EST LA CLE", False))


