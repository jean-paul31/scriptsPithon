import tarfile
import csv
import os



def extractFile(file):
    # Nom du fichier à décompresser
    nom_fichier = file

    # Ouverture du fichier en mode "lecture"
    fichier_tar = tarfile.open(nom_fichier, "r:gz")

    # Extraction des fichiers du fichier .tar.gz
    fichier_tar.extractall()

    # Fermeture du fichier
    fichier_tar.close()

def rename(file, repertoire):
    # Ouvrir le fichier CSV
    with open(file) as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)
        # Parcourir chaque ligne du fichier CSV
        for ligne_csv in lecteur_csv:
            # Obtenir le nom du fichier à partir de la colonne "filename"
            nom_fichier = ligne_csv["filename"]
            # Obtenir la valeur de l'id à partir de la colonne "id"
            id = ligne_csv["id"]
            # Parcourir les fichiers dans le répertoire racine
            for repertoire_racine, sous_repertoires, fichiers in os.walk(repertoire):
                # Parcourir chaque fichier dans le répertoire courant
                for nom_fichier_courant in fichiers:
                    # Vérifier si le nom du fichier courant correspond à la valeur de l'id
                    if nom_fichier_courant.startswith(id):
                        # Construire le nouveau nom de fichier à partir de la valeur de "filename"
                        nouveau_nom_fichier = os.path.join(repertoire_racine, nom_fichier)
                        # Renommer le fichier en utilisant le nouveau nom de fichier
                        chemin_courant = os.path.join(repertoire_racine, nom_fichier_courant)
                        os.rename(chemin_courant, nouveau_nom_fichier)

fileUnzip = input("Rentrer le nom du fichier à décompresser : ")

extractFile(fileUnzip)

fileCSV = input("Rentrer le nom du fichier CSV à parcourir : ")
repertoire = input("Indiquer le chemin de l'arborescence à parcourir : ")

rename(fileCSV, repertoire)

print(' \n La ré-attribution des noms de pj c\'est terminé avec succés \n')