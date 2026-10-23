# script pour le chiffrement et le déchiffrement par Vigenère
# l'alphabet utilisé est {A,B,C,D,...,Y,Z,espace}

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

    # on remplace le caractère espace par le caractère [ (le caractère [ a pour code 91)
    # cela permet de traiter le cas particulier de l'espace
    message = message.replace(" ", "[")
    
    i = 0
    for c in message : # on passe en revue tous les caractères du message
        if code :
            le_texte = le_texte+chr((((ord(cle[i]) - 65) + (ord(c) - 65)) % 27) + 65)
        else :
            le_texte = le_texte+chr(((-(ord(cle[i]) - 65) + (ord(c) - 65)) % 27) + 65)
        i += 1
        if i == len(cle): # on doit repartir du début de la clé
            i = 0

    # on rempace maintenant les [ par des espaces
    le_texte = le_texte.replace("[", " ")

    return(le_texte)



texte_en_clair = "ILS NE SAVAIENT PAS QUE C ETAIT IMPOSSIBLE ALORS ILS L ONT FAIT"
cle = "KPOXJK"
print(f"\nle texte en clair {texte_en_clair} avec la clé {cle}")
texte_chiffre = vigenere(texte_en_clair, cle, True)
print(f"\nle texte chiffré {texte_chiffre}")
print(f"\nle texte déchiffré {vigenere(texte_chiffre, cle, False)}")

# exemple de chiffrement et déchiffrement
#print(vigenere(vigenere("VOILA UN EXEMPLE AVEC UNE CLE", "ICI C EST LA CLE", True), "ICI C EST LA CLE", False))


