import zlib

try:
    # Lire le contenu du fichier
    with open('journal.txt', 'rb') as fichier:
        contenu = fichier.read()
   
    # Compression du contenu
    contenu_compresse = zlib.compress(contenu)
   
    # Affichage des tailles avant et après compression
    print(f"Taille avant compression : {len(contenu)} octets")
    print(f"Taille après compression : {len(contenu_compresse)} octets")
   
    # Sauvegarde du contenu compressé dans un nouveau fichier
    with open('journal_compressed.zlib', 'wb') as fichier_compresse:
        fichier_compresse.write(contenu_compresse)

except FileNotFoundError:
    print("Le fichier 'journal.txt' n'existe pas, impossible de le compresser.")
