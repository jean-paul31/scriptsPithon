from jira import JIRA
import requests
from requests.auth import HTTPBasicAuth
import json
import os
import getpass
"""
    Récupére les éléments utile à la connexion à jira 
"""

mail = input("Rentrer votre adresse mail : ")
mdp = getpass.getpass("Rentrer votre mot de passe : ")
server = input("Rentrer ici votre server fr/eu/ca/poc : ")
project_key = input("Rentrer ici votre project key : ")

"""
    |gestion des instances|DEBUT|
"""

server1 = "https://proactionfr.ent.cgi.com/jira"
server2 = "https://proactioneu.ent.cgi.com/jira"
server3 = "https://proactionca.ent.cgi.com/jira"
server4 = "https://proactioncapoc.ent.cgi.com/jira"

if server == 'fr':
    server = server1
elif server == 'eu':
    server = server2
elif server == 'ca':
    server = server3
elif server == 'poc':
    server = server4

"""
    |gestion des instances|FIN|
"""

# Initialisation de l'instance JIRA
options = {"server": server}
jira = JIRA(options, basic_auth=(mail, mdp))

# ID du projet Jira
project_id = project_key

# Récupération des tickets du projet
issues = jira.search_issues(f"project={project_id}", maxResults=False, fields="summary")

# création du dossier pour le projet
os.makedirs(project_id, exist_ok=True)

def commentaires(issues):
    """
        Enregistre tous les commentaires dans un fichier CSV
        ====================================================
        :Params issues: Liste des tickets 
    """
    csv_file_path = os.path.join(project_id, "commentaires.csv")
    # Création d'un fichier csv pour stocker les commentaires
    with open(csv_file_path, "w") as f:
        #Création des en-têtes
        f.write("issue_key, summary, comment, author, created\n")

        # Boucle à travers tous les tickets
        for issue in issues:
            # Récupération des commentaires de chaque ticket
            comments = jira.comments(issue)

            # Écriture des commentaires dans le fichier csv
            for comment in comments:
                f.write(f"{issue.key}, {issue.fields.summary}, {comment.body}, {comment.author.name}, {comment.created}\n")

#Execution de la Fonction
commentaires(issues)

print(' \n L\'extraction c\'est terminé avec succés \n')

