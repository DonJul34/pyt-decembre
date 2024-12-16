import os
import shutil

# Vérifier l'existence de 'journal.txt' et le copier
if os.path.exists('journal.txt'):
    shutil.copy('journal.txt', 'backup_journal.txt')
    print("'journal.txt' a été copié sous le nom 'backup_journal.txt'.")
else:
    print("Le fichier 'journal.txt' n'existe pas, impossible de le copier.")

